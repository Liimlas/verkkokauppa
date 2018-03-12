from django.shortcuts import render
from django.contrib import auth
from main.models import Game, BoughtGame, HighScore
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import *



@login_required
def play(request):

    owned_games = []

    if request.user.is_authenticated:
        bought_games = BoughtGame.objects.filter(owner=request.user)
        developed_games = Game.objects.filter(developer=request.user)
        for game in bought_games:
            owned_games.append(game.game)
        for game in developed_games:
            owned_games.append(game)

    return render(request, 'play/play.html', { 'games' : owned_games })


@login_required
@csrf_exempt
def playgame(request, gameid):

    if not request.user.is_authenticated():
        return redirect('/play/')

    try:
        found_game = Game.objects.get(id=gameid)
        highscores = []
        for score in HighScore.objects.filter(game=found_game):
            highscores.append(score)

        highscores.sort(key=lambda x: x.score, reverse=True)

        bought_games = []

        for bought_game in BoughtGame.objects.all():
            print("Hei")
            if bought_game.owner == request.user:
                bought_games.append(bought_game.game)

        for game in Game.objects.all():
            if game.developer == request.user:
                bought_games.append(game)

        if found_game in bought_games:
            return render(request, 'play/playgame.html', {'game': found_game, 'highscores': highscores[:10]})
        else:
            return render(request, 'play/playgame.html', {'game' : False, 'highscores' : highscores[:10]})

    except:
        return render(request, 'play/playgame.html', {'game' : None})


@login_required
@csrf_exempt
def save_scores(request):
    if request.method == "POST":
        game_score = float(request.POST.get('score', ''))
        game_id = request.POST.get('game_id', '')
        found_game = Game.objects.get(id=game_id)
        redir = '/play/' + game_id + '/'
        if game_score <= 0:
            return redirect('/play/')
        else:
            a = HighScore.objects.create(scorer=request.user, game=found_game, score=game_score)
            a.save()
            return redirect(redir)

    else:
        return redirect('/play/')
