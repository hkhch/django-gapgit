from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Tweet(models.Model):
    user_name = models.CharField(max_length = 30)
    contents = models.CharField(max_length = 300, null = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.user_name

    def recent(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days = 1)
	
	
