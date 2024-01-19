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

def game_status(game: Game, user):
    # 1. 유저가 a 일때
    if (game.player_a.nickname == user.nickname):
        # 1-a: 승부가 난 경우
        if (game.b_choice != None):
            if game.winner == user.nickname:
                return ["player_a", "승리"]
            elif game.winner == None:
                return ["player_a","무승부"]
            else:
                return ["player_a", "패배"]
        # 1-b: 상대 유저를 기다리는 경우
        else:
            return ["player_a", "진행중"]
    # 2. 유저가 b 일때
    else:
        ## 2-a: 승부가 난 경우
        if (game.b_choice != None):
            if game.winner == user.nickname:
                return ["player_b", "승리"]
            elif game.winner == None:
                return ["player_b","무승부"]
            else:
                return ["player_b","패배"]
        # 2-b: 반격 중인 경우
        else:
            return ["player_b", "반격중"]
    
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

    # game_status 가 추가된 데이터 
    games_with_status = []
    for game in games:
        status_result = game_status(game, request.user)
        games_with_status.append(
            {'game':game, 'player': status_result[0], 'result': status_result[1]})

    ctx = {'games': games_with_status}
    return render(request, 'games/games_list.html', ctx)

def detail(request, pk):
    '''
    pk: Game pk
    '''
    game = Game.objects.get(pk=pk)
    rule = mapping_rule(game.rule)
    result = game_status(game, request.user)
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

