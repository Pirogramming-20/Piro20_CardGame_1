from django.db import models
#from apps.users.models import user >유저 foreign key 가져오기

class Game(models.Model) :
    #player_a = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = '플레이어 A')
    #player_b =models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = '플레이어 B')
    a_choice = models.IntegerField('플레이어 A 선택 숫자')
    b_choice = models.IntegerField('플레이어 B 선택 숫자')
    rule = models.IntegerField('랜덤 규칙')
    winner = models.BooleanField(default=None)
