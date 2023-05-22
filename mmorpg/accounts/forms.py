import random

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from django.core.mail import send_mail


class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        if commit:
            user.save()
            common_users, created = Group.objects.get_or_create(name='player')
            user.groups.add(common_users)

        return user


class ConfirmationCodeForm(forms.Form):
    code = forms.CharField(max_length=6, label="Confirmation Code")
