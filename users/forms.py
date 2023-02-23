from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'password1': 'Hasło (min. 8 znaków, cyfry i litery)',
            'username': 'Nazwa',
            'email': 'Adres e-mail',
        }
