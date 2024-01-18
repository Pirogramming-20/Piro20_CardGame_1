from django.shortcuts import render, redirect
from .models import Game
from .forms import GameFormAttacker, GameFormDefender
import random
from apps.users.models import User
from django.db.models import Q


### utils ###
def select_rule():
    pass

def choose_winner(game: Game):
    if game.rule == 0: # 0이면 큰 숫자가 이김
        if game.a_choice > game.b_choice:
            game.winner = game.player_a.nickname
        elif game.b_choice > game.a_choice:
            game.winner = game.player_b.nickname
    elif game.rule == 1: # 1이면 작은 숫자가 이김
        if game.a_choice < game.b_choice:
            game.winner = game.player_a.nickname
        elif game.b_choice < game.a_choice:
            game.winner = game.player_b.nickname
    game.save()

def mapping_rule(rule):
    if rule == 0:
        return "숫자가 더 큰 사람이 대결에서 이깁니다"
    elif rule == 1:
        return "숫자가 더 작은 사람이 대결에서 이깁니다"
    
# 공격하기 페이지
def start(request):
    if request.method == 'POST':  
        form = GameFormAttacker(request.POST, user=request.user)
        if form.is_valid():
            game = form.save(commit=False)
            game.player_a = request.user
            game.rule = random.choice([0, 1])
            game.save()
        return redirect('games:game_list')
    else:
        form = GameFormAttacker(user=request.user)
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
    '''
    pk: Game pk
    '''
    game = Game.objects.get(pk=pk)
    rule = mapping_rule(game.rule)
    if request.user.nickname ==  game.winner:
        result = "승리"
    elif (game.winner == None) & (game.b_choice == None):
        result = "진행중"
    elif (game.winner == None) & (game.b_choice != None):
        print(f"game.winner: {game.winner}")
        result = "무승부"
    else:
        result = "패배"
    ctx = {"game": game, "result": result, "rule": rule}
    return render(request, 'games/games_detail.html', ctx)

def delete(request, pk):
    if request.method == "POST":
        Game.objects.get(id=pk).delete()
    return redirect('games:game_list')

def counterattack(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':  
        form = GameFormDefender(request.POST, instance=game)
        if form.is_valid():
            game = form.save()
            choose_winner(game)
        return redirect('games:game_list')
    else:
        form = GameFormDefender(instance=game)
        ctx = {"form": form, "pk": pk, "player_a": game.player_a}
        return render(request, 'games/games_counter.html', ctx)

