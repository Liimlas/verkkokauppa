from django.shortcuts import render
from main.models import Game
# Create your views here.


def list_of_ids(gamelist):
    ids = []
    for game in gamelist:
        ids.append(game.id)

    return ids

def games(request):
    context = {}
    context['gamelist'] = Game.objects.all()
    return render(request, 'gamesales/games.html', context)

def viewgame(request, id):
    context = {}
    context['in_list'] = False
    for game in Game.objects.all():
        if id == game.id:
            context['in_list'] = True
            context['game'] = game
    return render(request, 'gamesales/games.html', context)