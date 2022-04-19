from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from ..models.user_model import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)
