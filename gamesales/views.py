from django.shortcuts import render
from main.models import Game, BoughtGame
import random
import uuid

from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


from django.http import HttpResponseRedirect


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


@csrf_exempt
def addGame(request):
    # if post request came
    if request.method == 'POST':
        # getting values from post
        gamename = request.POST.get('name')
        gamedeveloper = request.POST.get('developer')
        gameprice = request.POST.get('price')
        gamelink = request.POST.get('link')
        gamePhotoLink = request.POST.get('photoLink')
        gameUsePhoto = request.POST.get('usePhoto')


        if len(gamename) < 3 or len(gamename) > 60:
            context = {}
            context['nameError'] = True
            return render(request, 'gamesales/addGame.html', context)
        elif gamedeveloper == 'no':
            context = {}
            context['developerError'] = True
            return render(request, 'gamesales/addGame.html', context)
        elif gamelink.find('.') == -1 and gamelink.find('www') == -1:
            context = {}
            context['linkError'] = True
            return render(request, 'gamesales/addGame.html', context)
        elif gamePhotoLink is not () and gameUsePhoto == 'yes':
            usePhoto()
            gameid = generate()
            context = {
                'name': gamename,
                'developer': gamedeveloper,
                'price': gameprice,
                'link': gamelink,
                'id': gameid,
                'photoLink': gamePhotoLink
            }
        else:
            gameid = generate()
            context = {
                'name': gamename,
                'developer': gamedeveloper,
                'price': gameprice,
                'link': gamelink,
                'id' : gameid,
                'photoLink': gamePhotoLink
            }

           # a = Game.objects.create(developer=request.user, name=gamename, id=gameid    , price=gameprice, saleprice=1, onsale=False, soldcopies=0, link=gamelink)
            #b = BoughtGame.objects.create(owner=request.user, game=a)
            #a.save()
            #b.save()

        # getting our showdata template
        return render(request, 'gamesales/showdata.html', context)
    else:
        # if post request is not true
        # returing the form template
        return render(request, 'gamesales/addGame.html')
