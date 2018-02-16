from django import forms
from .models import AddGame
#class PostForm(forms.Form):
 #   content = forms.CharField(max_length=256)
  #  created_at = forms.DateTimeField()



from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AddGameForm(forms.ModelForm):
    class Meta:
        model: AddGame
        #fields: ('Developer', 'title', 'description', 'price' )

