
from django.contrib import admin
from django.urls import path,include
from .views import Signup
urlpatterns = [
    #path('tweet', include('tweet.urls')),
    path('', Signup.as_view()),
    ]
