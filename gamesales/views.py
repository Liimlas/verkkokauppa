from django.shortcuts import render
from main.models import Game

from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


from django.http import HttpResponseRedirect



#from .forms import AddGame


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



#def addGame(request):
 #   return render(request, 'gamesales/addGame.html')




# disabling csrf (cross site request forgery)
@csrf_exempt
def addGame(request):
    # if post request came
    if request.method == 'POST':
        # getting values from post
        developer = request.POST.get('developer')
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')

        # adding the values in a context variable
        context = {
            'developer': developer,
            'title': title,
            'description': description,
            'price': price
        }

        # getting our showdata template
        template = loader.get_template('gamesales/showdata.html')

        # returing the template
        return HttpResponse(template.render(context, request))
    else:
        # if post request is not true
        # returing the form template
        template = loader.get_template('gamesales/addGame.html')
        return HttpResponse(template.render())
