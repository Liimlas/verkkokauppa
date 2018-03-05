from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from main.models import Game
from .models import Profile
from .forms import ProfileForm, UserCreationForm
from gamesales.forms import ChangeGameForm, DeleteNewForm
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from django.shortcuts import get_object_or_404
from django.utils import timezone
from gamesales.views import generate

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

    #Updates both profile- and user-instances witht the same form, takes user-fields defined in ProfileForm in forms.py
    #and profile- fields defined below
    ProfileInlineFormset = inlineformset_factory(User, Profile, fields=('birth_date', 'bio', 'photo'))
    formset = ProfileInlineFormset(instance=user)

    if request.user.is_authenticated() and request.user.pk == user.pk:
        if request.method == 'POST':
            user_form = ProfileForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(instance=user)

            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)

                #if creation is valid, updates both instances
                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return render(request, 'profile_updated.html')

        return render(request, 'update_profile.html', {
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
    #doesn't actually authenticate the user, but sends verification email to console
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user.profile.is_developer = form.cleaned_data.get('is_developer')
            user.save()
            user.profile.save()
            current_site = get_current_site(request)
            subject = 'Activate your account'
            message = render_to_string('verification/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = UserCreationForm()
    return render(request, 'signup/signup.html', {'form': form})

def activation_sent(request):
    return render(request, 'verification/activation_sent.html')

#activates the user when s/he clicks the link send to them via email
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    #if link is correct, activates user and logs in
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('index')
    else:
        return render(request, 'account_activation_invalid.html')

def manage_games(request):
    context = {'own_games': Game.objects.filter(developer = request.user)}
    return render(request, 'manage_games.html', context)

def edit(request):
    return render(request, 'managed_game.html')

def delete_game(request):
    return render(request, 'delete_game.html')

@csrf_exempt
def edit_game(request, pk):
    post = get_object_or_404(Game, pk=pk)
    post2 = get_object_or_404(Game, pk=pk)
    if request.method == "POST":
        form = ChangeGameForm(request.POST, instance=post)
        form2 = DeleteNewForm(request.POST, instance=post)
        if form.is_valid():
            gamedelete = request.POST.get('delete')
            gamesale = request.POST.get('sale')
            # if developer wants delete game
            if gamedelete == 'yes':
                if form2.is_valid():
                    post.delete()
                    return HttpResponseRedirect('/delete_game/')
            else:

                post = form.save(commit=False)
                post.developer = request.user

                context = {}

                # radio button check that if game is on sale
                # -> onsale is true and gamesale has two decimal
                if gamesale == 'yes' and post.saleprice != 0:
                    post.saleprice = format(( 1 - post.saleprice) *
                                               post.price,'.2f')
                    post.onsale = True
                else:
                    post.saleprice = 0
                    post.onsale = False
                post.soldcopies = 0
                post.save()

                return HttpResponseRedirect('/managed_game/')
           #      New.objects.get(pk=id).delete()

    else:
        #z = (1-x)*y -> (z/y)-1 = -x -> x = -(z/y)+1
        if post.onsale == False:
            post.saleprice = 0.0
        else:
            post.saleprice = format(-(post.saleprice / post.price)+1,'.2f')

        form = ChangeGameForm(instance=post)
    return render(request, 'edit_game.html', {'form': form})





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
