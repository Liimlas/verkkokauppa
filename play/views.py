from django.shortcuts import render
from django.contrib import auth
from main.models import Game, BoughtGame, HighScore, GameState
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .forms import *
import json



@login_required
def play(request):

    owned_games = []

    if request.user.is_authenticated:
        bought_games = BoughtGame.objects.filter(owner=request.user)
        developed_games = Game.objects.filter(developer=request.user)
        for game in bought_games:
            owned_games.append(game.game)
        for game in developed_games:
            owned_games.append(game)

    return render(request, 'play/play.html', { 'games' : owned_games })


@login_required
@csrf_exempt
def playgame(request, gameid):

    if not request.user.is_authenticated():
        return redirect('/play/')

    try:
        found_game = Game.objects.get(id=gameid)
        highscores = []
        for score in HighScore.objects.filter(game=found_game):
            highscores.append(score)

        highscores.sort(key=lambda x: x.score, reverse=True)

        bought_games = []

        for bought_game in BoughtGame.objects.all():
            if bought_game.owner == request.user:
                bought_games.append(bought_game.game)

        for game in Game.objects.all():
            if game.developer == request.user:
                bought_games.append(game)

        if found_game in bought_games:
            return render(request, 'play/playgame.html', {'game': found_game, 'highscores': highscores[:10]})
        else:
            return render(request, 'play/playgame.html', {'game' : False, 'highscores' : highscores[:10]})

    except:
        return render(request, 'play/playgame.html', {'game' : None})


@login_required
@csrf_exempt
def save_scores(request):
    try:
        game_id = request.POST.get('game_id')
        score = float(request.POST.get('score'))
        game_by_id = Game.objects.get(id=game_id)

        if score <= 0:
            return JsonResponse({"Message" : "You have to have more than 0 points to save the highscores!"})

        new_score = HighScore.objects.create(scorer=request.user, score=score, game=game_by_id)
        new_score.save()

        message = "Added a new highscore of " + str(score) + " points!"
        return JsonResponse({"Message": message})
    except:
        return JsonResponse({"Message" : "Could not save highscores, something went wrong!"})

@login_required
@csrf_exempt
def save_state(request):
    try:
        game_id = request.POST.get('game_id')
        game_state = request.POST.get('game_state')
        game_by_id = Game.objects.get(id=game_id)

        state = GameState.objects.filter(player=request.user).filter(game=game_by_id)

        if not state:
            new_state = GameState.objects.create(player=request.user, game=game_by_id, game_state=game_state)
            new_state.save()
            return JsonResponse({"Message" : "Successfully created a new state!"})

        else:
            modified_state = state[0]
            modified_state.game_state = game_state
            modified_state.save()
            return JsonResponse({"Message" : "Successfully saved new state"})

    except:
        return JsonResponse({"Message" : "Something went wrong, could not save the data!"})


@login_required
@csrf_exempt
def load_state(request):
    try:
        a = GameState.objects.all()

        game_id = request.GET.get('game_id')
        game_by_id = Game.objects.get(id=game_id)

        filtered_game_states = a.filter(player=request.user).filter(game=game_by_id)[0]

        if not filtered_game_states:
            message = {
                "messageType": "ERROR",
                "info": "Could not find saved state for this user!",
                "Message" : "Could not find saved state for this user!"
            }
            return JsonResponse(message)

        else:
            message = {
                "messageType": "LOAD",
                "gameState" : json.loads(filtered_game_states.game_state),
                "Message" : "Succesfully loaded the data"
            }
            return JsonResponse(message)
    except:
        message = {
            "messageType": "ERROR",
            "info": "Could not load the game info!",
            "Message": "Could not load the game info!"

        }

        return JsonResponse(message)
