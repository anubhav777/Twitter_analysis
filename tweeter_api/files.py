import tweepy
import json
from datetime import time,datetime
from .serializers import Twittimelineseril
from .models import Tweet_users
import re
consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True,parser=tweepy.parsers.JSONParser())
tweets_list = []
user_list=[]
user_search=[]
text_query = ''
count = 5

def text_filter(text):
    emoji_pattern = re.compile("["
       u"\U0001F600-\U0001F64F"  # emoticons
       u"\U0001F300-\U0001F5FF"  # symbols & pictographs
       u"\U0001F680-\U0001F6FF"  # transport & map symbols
       u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
       u"\U00002702-\U000027B0"
       u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    text=emoji_pattern.sub(r'', text)
    text=re.sub(r'@[_A-Za-z0-9]+','',text)
    text=re.sub(r'#[A-Za-z0-9]+','',text)
    text=re.sub(r'RT[\s]+','',text)
    text=re.sub(r'https?:\/\/[a-zA-Z0-9].[a-z]+\/[a-zA-Z0-9]+','',text)
    text=re.sub(r':','',text)
    text=re.sub('  +',' ',text)
    text=re.sub(r'&[a-zA-Z0-9]+;?','',text)
    text=re.sub(r', +','',text)
  
    return text

def search_func(text_query):
    results=api.search(q=text_query, count=count, tweet_mode='extended')
    # print(results['statuses'][0].keys())

    for i in range(len(results['statuses'])):
    
        new_results=results['statuses']
        try:
        # Pulling individual tweets from query
            arr_keys=new_results[i].keys()
            
            new_user=None
            retweet_count=None
            favorite_count=None
            if 'retweeted_status' in arr_keys:
            
                new_user=new_results[i]['retweeted_status']['user']
                retweet_count=new_results[i]['retweeted_status']['retweet_count']
                favorite_count=new_results[i]['retweeted_status']['favorite_count']

            else:
                new_user=new_results[i]['user']
                retweet_count='No retweet available'
                favorite_count='No favourite avialable'
            tweet_id=new_results[i]['id']
            text=new_results[i]['full_text']
            tweeter_name=new_user['name']
            tweeter_screen_name=new_user['screen_name']
            following=new_user['friends_count']
            followers=new_user['followers_count']
            profile_pic=new_user['profile_image_url']
            cover_photo=None
            try:
                cover_photo=new_user['profile_banner_url']
            except: 
                cover_photo="No Cover Photo"
            location=new_user['location']
            language=new_results[i]['lang']
            hastag_parent=new_results[i]['entities']['hashtags']
            media_data=None
            entities=new_results[i]['entities'].keys()
            if 'media' in entities:
                # print(new_results[i]['entities']['media'])
                media_data=new_results[i]['entities']['media'][0]['media_url']
            else:
                media_data='No medias'
            url=None
            if len(new_results[i]['entities']['urls']) > 1 :
                url=e,nw_results[i]['entities']['urls'][0]['url']
            else:
                url='No url'
            old_created_time=new_results[i]['created_at']
            created_time=datetime.strptime(old_created_time,'%a %b %d %H:%M:%S %z %Y')
            new_created_time=created_time.strftime('%Y-%m-%d')
            new_text=text_filter(text)
            print(text)
            print(new_text,tweeter_screen_name)
            # favorited=new_results[0]['favorited']
            hastag=[]
            try:
                for i in range(len(hastag_parent)):
                    new_hashtag=f"#{hastag_parent[i]['text']}"
                    hastag.append(new_hashtag)
            except :
                pass
            users={'tweeter_name':tweeter_name,'tweeter_screen_name':tweeter_screen_name,'following':following,'followers':followers,'profile_pic':profile_pic,'cover_photo':cover_photo,'location':location}
            all_data={'tweet_id':tweet_id,'text':text,'created_time':new_created_time,'hastag':hastag,'users':users,'media_data':media_data,'url':url,'retweet_count':retweet_count,'favorite_count':favorite_count,'language':language}
            tweets_list.append(all_data)
        
            
        except BaseException as e:
            print('failed on_status,',str(e))

search_func(text_query)

def singleuser_timeline(fkid):
    results=api.user_timeline(screen_name='@nike',count=20,tweet_mode='extended')
   
    for i in range(len(results)):
        try:
            base_url=results[i]
            created_date=base_url['created_at']
            created_time=datetime.strptime(created_date,'%a %b %d %H:%M:%S %z %Y')
            new_created_time=created_time.strftime('%Y-%m-%d')
            entities=base_url['entities'].keys()
            media_data=None
            if 'media' in entities:
                media_data=base_url['entities']['media'][0]['media_url']
            else:
                media_data='No medias'
            url=None
            if len(base_url['entities']['urls']) > 1 :
                url=base_url['entities']['urls'][0]['url']
            else:
                url='No url'
        
            text=base_url['full_text']
            # new_text=None
            # if url in text:
            #     print('ho')
            #     new_text=text.replace(url,'')
            # else:
            #     new_text=text

            base_user=base_url['user']
            uniqueid=base_url['id']
            user_id=base_user['id']
            user_name=base_user['name']
            screen_name=base_user['screen_name']
            following=base_user['friends_count']
            followers=base_user['followers_count']
            profile_image_url=base_user['profile_image_url']
            retweet_count=int(base_url['retweet_count'])
            favorite_count=int(base_url['favorite_count'])
            hastag_parent=base_url['entities']['hashtags']
            hastag={}
            try:
                    for i in range(len(hastag_parent)):
                        new_hashtag=f"#{hastag_parent[i]['text']}"
                        hastag.update(new_hashtag)
            except :
                    pass
            user_details={'user_id':user_id,'user_name':user_name,'screen_name':screen_name,'following':following,'followers':followers,'profile_image_url':profile_image_url}
            all_data={'text':text,'uniqueid':uniqueid,'created_date':new_created_time,'url':url,'media_data':media_data,'user_details':user_details,'retweet_count':retweet_count,'favourite_count':favorite_count,'hashtag':hastag,'tweetid':fkid}
            check_data=None
            try:
                check_data=Tweet_users.objects.get(uniqueid=uniqueid)
            except :
                pass
            if check_data == None:
                serializer=Twittimelineseril(data=all_data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(serializer.errors)
            else:
                serializer=Twittimelineseril(check_data,data=all_data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(serializer.errors)
            user_list.append(all_data)

        except BaseException as e:
            print(e)

# singleuser_timeline(2)
# print(user_list)
def search_user():
    results=api.search_users(q='@nike',count=10)
    print(len(results))
    # for i in range(len(results)):
    #     name=results[i]['name']
    #     profile_image_url=results[i]['profile_image_url']
    #     followers=results[i]['followers_count']
    #     screen_name=results[i]['screen_name']
    #     user_id=results[i]['id']
    #     all_data={'user_id':user_id,'name':name,'screen_name':screen_name,'followers':followers,'profile_image_url':profile_image_url}
    #     user_search.append(all_data)
    i=0
    name=results[i]['name']
    profile_image_url=results[i]['profile_image_url']
    followers=results[i]['followers_count']
    screen_name=results[i]['screen_name']
    user_id=results[i]['id']
    all_data={'user_id':user_id,'name':name,'screen_name':screen_name,'followers':followers,'profile_image_url':profile_image_url}        
    return all_data
   

# print(user_search)

