from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from main.models import Game

@login_required
def profile(request):
    context = { 'games': Game.objects.filter(developer=request.user) }
    return render(request, 'profile.html', context)

@login_required
def profiles(request):
    context = { 'profiles' : User.objects.all() }
    return render(request, 'profiles.html', context)

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


# Create your views here.
