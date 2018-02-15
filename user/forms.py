from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2', )

class ProfileForm(forms.ModelForm):
    class Meta:
        model: Profile
        fields: ('birth_date', 'bio', 'is_developer', )

        def save(self, user=None):
            user_profile = super(UserProfileForm, self).save(commit=False)
            if user:
                user_profile.user = user
            user_profile.save()
            return user_profile
