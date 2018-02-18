from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import Game
from .models import Profile


@login_required
def profile(request):
    context = { 'games': Game.objects.filter(developer=request.user) }
    return render(request, 'view_user.html', context)

@login_required
def profiles(request):
    context = { 'profiles' : User.objects.all() }
    return render(request, 'profiles.html', context)

@login_required
@csrf_exempt
def update_profile(request):
    if request.method == 'POST':
        context = { 'games': Game.objects.filter(developer=request.user) }

        email = request.POST.get('email')
        bio = request.POST.get('bio')
        birth_date = request.POST.get('birth_date')
        is_developer = request.POST.get('is_developer')

        profile = request.user

        profile.email = email or profile.email
        profile.profile.bio = bio or profile.profile.bio
        profile.profile.birth_date = birth_date or profile.profile.birth_date

        if (is_developer == "yes"):
            profile.profile.is_developer = True
        else:
            profile.profile.is_developer = False

        profile.save()
        return render(request, 'profile.html', context)
    else:
        return render(request, 'update_profile.html')

@login_required
def viewUser(request, username):
    viewer = request.user
    context = {}
    context['not_found'] = True
    for user in User.objects.all():
        if username == user.username:
            context['userfound'] = True
            context['viewUser'] = user
            context['games'] = Game.objects.filter(developer=user)
    return render(request, 'view_user.html', context)



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

def manage_games(request):
    return render(request, 'manage_games.html')


# Create your views here.
