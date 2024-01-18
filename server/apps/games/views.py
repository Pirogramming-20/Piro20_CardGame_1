from django.shortcuts import render, redirect
from .models import Game
from .forms import GameFormAttacker
import random
from apps.users.models import User
from django.db.models import Q

def select_rule():
    pass
# 공격하기 페이지
def start(request):
    if request.method == 'POST':  
        form = GameFormAttacker(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.player_a = request.user
            game.rule = random.choice([0, 1])
            game.save()
            pass # game_list로 redirect
    else:
        form = GameFormAttacker()
        ctx = {"form": form}
        return render(request, 'games/games_start.html', ctx)

def game_list(request):
    user_nickname = request.user.nickname
    games = Game.objects.filter(Q(player_a__nickname=user_nickname) | Q(player_b__nickname=user_nickname))
    ctx = {'games': games}
    return render(request, 'games/games_list.html', ctx)

def detail(request, pk):
    #ajax로 창 안쪽 내용만 바꿔야 할듯
    #1.게임이 끝났을 경우 - 3번 / 2. 게임이 안끝난 나의 입장 - 1번 / 3. 게임이 안끝난 상대 입장 - 2번
    pass

def delete(request, pk):
    if request.method == "POST":
        Game.objects.get(id=pk).delete()
    return redirect('games:game_list')

def counterattack(request, pk):
    pass
