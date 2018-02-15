from django.shortcuts import render
from main.models import Game
# Create your views here.

#from django.shortcuts import render
#from django.http import HttpResponseRedirect

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

#    if request.method == 'POST':

 #       form = AddGame(request.POST)

  #      if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
          #  return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
   # else:
    #    form = AddGame()

    #return render(request, 'addGame.html') #, {'form': form})
#def addGame(request):
 #   gamelist += request
  #  return render(request, 'gamesales/addGame.html')


def addGame(request):
    return render(request, 'gamesales/addGame.html')
