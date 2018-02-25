from django import forms
from main.models import Game
from django.forms import ModelForm

class AddGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('name', 'price', 'link', 'image')


class ChangeGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('name', 'price', 'link', 'image', 'saleprice')


class DeleteNewForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = []

