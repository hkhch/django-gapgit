
from django.contrib import admin
from django.urls import path,include
from .views import Tweets
urlpatterns = [
    #path('tweet', include('tweet.urls')),
    path('', Tweets.as_view()),
    ]
