
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('tweeti/', include('tweet.urls')),
    path('signup/', include('signup.urls')),
    path('login/', include('login.urls'))
    ]
