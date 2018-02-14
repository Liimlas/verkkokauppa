
from django.shortcuts import render
from main.models import Game
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm



# Gives a sorted list back according to a given attribute. e.g. amount of sold copies or price, etc
def games_by_attribute(gamelist, attribute, reversed):
    games_sorted = []
    for game in gamelist:
        games_sorted.append(game)

    if(attribute == 0): #Sort by name
        games_sorted.sort(key=lambda x: x.name, reverse=reversed)
    elif(attribute == 1): #Sort by price
        games_sorted.sort(key=lambda x: x.price, reverse=reversed)
    elif(attribute == 2): #Sort by soldcopies
        games_sorted.sort(key=lambda x: x.soldcopies, reverse=reversed)
    elif(attribute == 3): #Sort by sale price
        games_sorted.sort(key=lambda x: x.saleprice, reverse=reversed)

    return games_sorted



def index(request):
    context = { 'games' : games_by_attribute(Game.objects.all(), 3, False) }
    return render(request, 'frontpage/index.html', context)

@login_required
def profile(request):
    return render(request, 'frontpage/profile.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup/signup.html', {'form': form})
