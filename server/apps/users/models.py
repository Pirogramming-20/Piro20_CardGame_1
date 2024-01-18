from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    user_id = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    nickname = models.CharField(max_length=16)
    score = models.IntegerField(default = 0)
    def __str__(self):
        return self.nickname