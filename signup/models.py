from django.db import models

# Create your models here.

class Account(models.Model):
    user_id = models.CharField(max_length = 30, unique = True)
    user_name = models.CharField(max_length = 30)
    password = models.CharField(max_length = 20)
    profile = models.CharField(max_length = 200, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.user_id
