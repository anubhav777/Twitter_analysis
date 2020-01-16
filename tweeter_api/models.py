from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField
# Create your models here.
class Tweet_users(models.Model):
    user_id=models.CharField(max_length=128,unique=True)
    screen_name=models.CharField(max_length=129)
    name=models.CharField(max_length=128)
    profile_image_url=models.CharField(max_length=128)
    followers=models.CharField(max_length=128)
class Tweettimeline(models.Model):
    uniqueid=models.CharField(max_length=128,blank=True)
    text=models.CharField(max_length=500)
    created_date=models.DateField(default=timezone.now,blank=True)
    url=models.CharField(max_length=300)
    media_data=models.CharField(max_length=300)
    user_details=JSONField(blank=True,default=dict)
    retweet_count=models.IntegerField(default=0)
    favourite_count=models.IntegerField(default=0)
    hashtag=JSONField(blank=True,default=dict)
    tweetid=models.ForeignKey('Tweet_users',on_delete=models.CASCADE)
    