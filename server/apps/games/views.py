from django.shortcuts import render
from .models import Game

def start(request):
    pass

def game_list(request):
    pass

def detail(request, pk):
    #ajax로 창 안쪽 내용만 바꿔야 할듯
    #1.게임이 끝났을 경우 - 3번 / 2. 게임이 안끝난 나의 입장 - 1번 / 3. 게임이 안끝난 상대 입장 - 2번
    pass

def delete(request, pk):
    pass

def counterattack(request, pk):
    pass
