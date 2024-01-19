from django.urls import path
from .views import *

app_name = 'games'

urlpatterns = [
    path('start/', start, name="start"), #3. 공격하기 페이지
    path('game_list/', game_list, name="game_list"), #4. 게임 list 페이지
    path('detail/<int:pk>/', detail, name="detail"), #5. 게임 detail 페이지
    path('delete/<int:pk>/', delete, name="delete"),
    path('counterattack/<int:pk>/', counterattack, name='counterattack'), #반격하기 페이지
    path('game_ranking/', ranking, name="game_ranking"),
]
