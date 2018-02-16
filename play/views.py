from django.shortcuts import render
from django.contrib import auth
from main.models import Game, BoughtGame


def play(request):
    context = {}
    if request.user.is_authenticated():
        bought_games = BoughtGame.objects.filter(owner=request.user)
        owned_games = []
        for game in bought_games:
            owned_games.append(game.game)
        context['games'] = owned_games

    return render(request, 'play/play.html', context)

def playgame(request, gameid):
    context = {}
    lista = []
    game = Game.objects.filter(id=gameid)
    for g in game:
        lista.append(g)
    context['game'] = lista[0]
    return render(request, 'play/playgame.html', context)

