from django.contrib.auth.models import User
from django import forms
from .models import UserProfile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('nickname',)