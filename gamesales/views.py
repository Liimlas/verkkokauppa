from django.shortcuts import render, redirect
from main.models import Game, BoughtGame
from .forms import AddGameForm
import random
from django.utils import timezone
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

def usePhoto():
    photoList = Game.objects.all()
    photos = []
    for photo in photoList:
        photos.append(photo.photoLink)
    return photos
    # do it the way that photo is in the home page


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

# @csrf_exempt
# def addGame(request):
#     # if post request came
#     if request.method == 'POST':
#         # getting values from post
#         gamename = request.POST.get('name')
#         gamedeveloper = request.POST.get('developer')
#         gameprice = request.POST.get('price')
#         gamelink = request.POST.get('link')
#         gamePhotoLink = request.POST.get('photoLink')
#         gameUsePhoto = request.POST.get('usePhoto')


#         if len(gamename) < 3 or len(gamename) > 60:
#             context = {}
#             context['nameError'] = True
#             return render(request, 'gamesales/addGame.html', context)
#             return render(request, 'gamesales/addGame.html', context)
#         elif gamelink.find('.') == -1 and gamelink.find('www') == -1:
#             context = {}
#             context['linkError'] = True
#             return render(request, 'gamesales/addGame.html', context)
#         else:
#             gameid = generate()
#             context = {
#                 'name': gamename,
#                 'price': gameprice,
#                 'link': gamelink,
#                 'id' : gameid,
#                 'photoLink': gamePhotoLink
#             }

#             a = Game.objects.create(developer=request.user, name=gamename, id=gameid, price=gameprice, saleprice=1, onsale=False, soldcopies=0, link=gamelink, publish_date=timezone.now())
#             b = BoughtGame.objects.create(owner=request.user, game=a)
#             a.save()
#             b.save()


#         # getting our showdata template
#         return render(request, 'gamesales/showdata.html', context)
#     else:
#         # if post request is not true
#         # returing the form template
#         return render(request, 'gamesales/addGame.html')

def onSale(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'gamesales/gameonsale.html', context)
