from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from main.models import Game
from .models import Profile
from .forms import ProfileForm

@login_required
def profile(request):
    context = { 'games': Game.objects.filter(developer=request.user) }
    return render(request, 'view_user.html', context)

@login_required
def profiles(request):
    context = { 'profiles' : User.objects.all() }
    return render(request, 'profiles.html', context)

@login_required
def update_profile(request, pk):
    user = User.objects.get(pk=pk)
    user_form = ProfileForm(instance=user)
    context = { 'games': Game.objects.filter(developer=request.user) }

    ProfileInlineFormset = inlineformset_factory(User, Profile, fields=('birth_date', 'bio', 'is_developer', 'photo'))
    formset = ProfileInlineFormset(instance=user)

    if request.user.is_authenticated() and request.user.pk == user.pk:
        if request.method == 'POST':
            user_form = ProfileForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(instance=user)

            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)

                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return HttpResponseRedirect('/profile/')

        return render(request, "update_profile.html", {
            'noodle': pk,
            'noodle_form': user_form,
            'formset': formset,
        })
    else:
        raise PermissionDenied

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


def model_form_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ImageForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })

# Create your views here.
