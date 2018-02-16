from django.shortcuts import render
from main.models import Game
import uuid


from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


from django.http import HttpResponseRedirect



#from .forms import AddGame


def list_of_ids():
    gamelist = Game.objects.all()
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



#def addGame(request):
 #   return render(request, 'gamesales/addGame.html')
def generate():
    existing_ids = list_of_ids()
    newid = uuid.uuid4()
    while(True):
        if newid in existing_ids:
            newid = uuid.uuid4()
        else:
            return newid


@csrf_exempt
def addGame(request):
    # if post request came
    if request.method == 'POST':
        # getting values from post

        name = request.POST.get('name')
        developer = request.POST.get('developer')
        price = request.POST.get('price')
        link = request.POST.get('link')


        if len(name) < 3 or len(name) > 60:
            context = {}
            context['nameError'] = True
            return render(request, 'gamesales/addGame.html', context)
        elif developer == 'no':
            context = {}
            context['developerError'] = True
            return render(request, 'gamesales/addGame.html', context)
        elif link.find('.') == -1 and link.find('www') == -1:
            context = {}
            context['linkError'] = True
            return render(request, 'gamesales/addGame.html', context)
        else:
            context = {

                'name': name,
                'developer': developer,
                'price': price,
                'link': link
            }

        # getting our showdata template
        return render(request, 'gamesales/showdata.html', context)
    else:
        # if post request is not true
        # returing the form template
        return render(request, 'gamesales/addGame.html')
