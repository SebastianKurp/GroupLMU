from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput) # widget needed so it doesnt show password


    # meta class is info about the class itself
    class Meta:
        model = User
        # user is django default table you see on admin screen
        fields = [
            'username',
            'email',
            'password',
        ]