from django.shortcuts import render
from main.models import Game
# Create your views here.


def list_of_ids(gamelist):
    ids = []
    for game in gamelist:
        ids.append(game.id)

    return ids

def games(request):
    games = Game.objects.all()
    context = {'pageview' : True, 'games' : games}
    return render(request, 'gamesales/games.html', context)

def viewgame(request, id):
    context = {}
    context['not_found'] = True
    for game in Game.objects.all():
        if id == game.id:
            context['gamefound'] = True
            context['game'] = game
    return render(request, 'gamesales/games.html', context)
