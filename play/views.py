from django.shortcuts import render
from django.contrib import auth
from main.models import Game, BoughtGame
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

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


def playgame(request, gameid):
    if not request.user.is_authenticated():
        return redirect('/play/')

    exists = Game.objects.filter(id=gameid)

    if not exists:
        return render(request, 'play/playgame.html', {'game' : None})

    owned_game = None
    bought_games = BoughtGame.objects.filter(owner=request.user)
    developed_games = Game.objects.filter(developer=request.user)

    for game in bought_games:
        if game.game.id == gameid:
            owned_game = game.game

    if owned_game == None:
        for game in developed_games:
            if game.id == gameid:
                owned_game = game

    return render(request, 'play/playgame.html', { 'game' : owned_game })