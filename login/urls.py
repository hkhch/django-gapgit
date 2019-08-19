
from django.contrib import admin
from django.urls import path,include
from .views import login_post
urlpatterns = [
    path('', login_post.as_view()),
    ]
