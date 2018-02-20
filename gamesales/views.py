from django.shortcuts import render, redirect
from main.models import Game, BoughtGame
from .forms import AddGameForm
import random
from django.utils import timezone
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def games(request):
    games = Game.objects.all()
    context = {'games' : games}
    return render(request, 'gamesales/games.html', context)

def viewgame(request, id):
    viewer = request.user
    context = {}
    context['not_found'] = True
    for game in Game.objects.all():
        if id == game.id:
            context['gamefound'] = True
            context['game'] = game
    return render(request, 'gamesales/singlegame.html', context)


def list_of_ids():
    gamelist = Game.objects.all()
    ids = []
    for game in gamelist:
        ids.append(game.id)
    return ids


#def addGame(request):
#   return render(request, 'gamesales/addGame.html')
def generate():
    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHILJKLMNOPQRSTUVWXYZ0123456789")
    letter_list_size = len(letters)
    existing_ids = list_of_ids()
    id = ''
    while(True):
        while(len(id) < 20):
            random_letter_index = random.randrange(0, letter_list_size - 1)
            id += letters[random_letter_index]
        if id in existing_ids:
            id = ''
        else:
            return id

def addGame(request):
    if request.method == 'POST':
        form = AddGameForm(request.POST, request.FILES)
        context= {}

        if form.is_valid():
            newGame = form.save(commit=False)
            newGame.developer = request.user
            newGame.saleprice = 0
            newGame.onsale = False
            newGame.soldcopies = 0
            newGame.publish_date = timezone.now()

            newID = generate()
            newGame.id = newID
            newGame.save()

            return redirect('index')
    else:
        form = AddGameForm()

    return render(request, 'gamesales/addGame.html', {'form': form})

def onSale(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'gamesales/gameonsale.html', context)
