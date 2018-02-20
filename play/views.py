from django.shortcuts import render
from django.contrib import auth
from main.models import Game, BoughtGame
from django.shortcuts import redirect


def play(request):
    owned_games = []

    if request.user.is_authenticated:
        bought_games = BoughtGame.objects.filter(owner=request.user)
        for game in bought_games:
            owned_games.append(game.game)

    return render(request, 'play/play.html', { 'games' : owned_games })


def playgame(request, gameid):
    if not request.user.is_authenticated():
        return redirect('/play/')

    exists = Game.objects.filter(id=gameid)

    if not exists:
        return render(request, 'play/playgame.html', {'game' : None})

    owned_game = None
    owned_games = BoughtGame.objects.filter(owner=request.user)

    for game in owned_games:
        if game.game.id == gameid:
            owned_game = game.game

    return render(request, 'play/playgame.html', { 'game' : owned_game })