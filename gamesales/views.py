from django.shortcuts import render, redirect
from main.models import Game, BoughtGame
from .forms import AddGameForm
import random
from django.utils import timezone
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from itertools import chain
# Create your views here.


def games(request):
    games = Game.objects.all()

    ownedGames = []
    boughtGames = []
    # Needed for knowing whether to show buy- button or not
    # (doesn't shot it if you already own the game)
    if request.user.is_authenticated:
        boughtGames = BoughtGame.objects.filter(owner=request.user)

        for purchase in boughtGames:
            ownedGames.append(purchase.game)

        for game in games:
            if game.developer == request.user:
                ownedGames.append(game)

    context = {
        'games' : games,
        'ownedGames': ownedGames,
        'bought': boughtGames
    }

    return render(request, 'gamesales/games.html', context)

def viewgame(request, id):
    context = {}
    dates = []
    context['not_found'] = True
    alreadyOwned = False



    for game in Game.objects.all():
        number = 1
        index = 0
        if id == game.id:

            # checks if you are signed in and already own the game,
            # and decides which button play/buy to show
            if request.user.is_authenticated:
                ownedSet = BoughtGame.objects.filter(owner=request.user,game=game)
                gameDate = BoughtGame.objects.filter(game=game)

                if ownedSet.count() != 0 or game.developer == request.user:
                    alreadyOwned = True
                    if game.developer == request.user:

                        for gamedate in gameDate:
                            if dates[index] is not gamedate.date:
                                dates.append(gamedate.date)
                                index += 1
                            else:
                                dates.append(number +1)
                                index += 1


            context['gamefound'] = True
            context['game'] = game
            context['alreadyOwned'] = alreadyOwned

    context['sold'] = dates
    if len(dates) == 0:
        context['zeroBought'] = True
    elif len(dates) == 1:
        context['oneBought'] = True
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

def added_game(request):
    return render(request, 'gamesales/showdata.html')


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

            return HttpResponseRedirect('/addedGame/')
    else:
        form = AddGameForm()

    return render(request, 'gamesales/addGame.html', {'form': form})


def onSale(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'gamesales/gameonsale.html', context)
