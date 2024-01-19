from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_id = models.CharField(max_length=16, blank=True)
    password = models.CharField(max_length=16)
    # nickname = models.CharField(max_length=16, unique=True, blank =False)
    score = models.IntegerField(default = 0)

    # def __str__(self):
    #     return self.username
    
class SocialUser(models.Model):
    sns_id = models.CharField(max_length=16)
    sns_nickname = models.CharField(max_length=16)
    user_pk = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='유저번호')

