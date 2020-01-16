from rest_framework import serializers
from .models import Tweet_users,Tweettimeline

class Twitteruserseril(serializers.ModelSerializer):
    class Meta:
        model=Tweet_users
        fields=('id','user_id','screen_name','name','profile_image_url','followers')

class Twittimelineseril(serializers.ModelSerializer):
    class Meta:
        model=Tweettimeline
        fields=('id','uniqueid','text','created_date','url','media_data','user_details','retweet_count','favourite_count','hashtag','tweetid')