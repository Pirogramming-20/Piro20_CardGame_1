from django.db import models
from apps.users.models import User


class Game(models.Model):
    player_a = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='player_a', verbose_name='플레이어 A')
    player_b = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='player_b', verbose_name='플레이어 B')
    a_choice = models.IntegerField('플레이어 A 선택 숫자')
    b_choice = models.IntegerField('플레이어 B 선택 숫자', null=True)
    rule = models.IntegerField('랜덤 규칙')
    winner = models.CharField(default=None, null=True, max_length=16)
