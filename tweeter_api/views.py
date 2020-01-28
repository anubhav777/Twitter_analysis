from django.shortcuts import render
from rest_framework import viewsets,status,permissions
from rest_framework.decorators import action,api_view,permission_classes
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.http import HttpResponse
from datetime import date
from datetime import datetime,date
from .files import *
from .serializers import Twitteruserseril
from .models import Tweet_users

# Create your views here.
@api_view(['POST'])
def insert_user(request):
    user_data=search_user()
    print(user_data)
    serializers=Twitteruserseril(data=user_data)
    if serializers.is_valid():
        serializers.save()
    else:
        print(serializers.errors)
    return Response({'status':'hi'})

@api_view(['POST'])
def insert_timeline(request):
    tweet=request.META['HTTP_TWEETID']
    print(tweet)
    tweet_id=Tweet_users.objects.get(user_id=tweet)
    call_func=singleuser_timeline(tweet_id.id)
    print(tweet_id.id)
    return Response({'status':'hi'})
    