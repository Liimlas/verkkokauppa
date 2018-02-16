from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.forms import ModelForm

class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2', )

class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'is_developer', 'birth_date', )
