from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User, Group
from django.urls import reverse_lazy
from django.utils.crypto import get_random_string
from django.views import View
from django.views.generic.edit import CreateView, FormView
from .forms import UserForm, ConfirmationCodeForm
from django.core.mail import send_mail
from django.conf import settings

import random

from django.contrib.auth.models import User

from .models import Profile


class SignUp(CreateView):
    model = User
    form_class = UserForm
    template_name = 'registration/signup.html'
    success_url = 'confirm'

    def form_valid(self, form):
        """ Генерируем код подверждения
            Сохраняем кодв базе данных
            Отправляем код пользователю на эмейл """

        user = form.save()

        Profile.objects.create(user=user)
        code = get_random_string(length=5)
        profile = Profile.objects.get(user=user)
        profile.confirmation_code = code
        profile.save()
        send_mail(
            'Код подтверждения',
            f'Ваш код подтверждения: {code}',
            'noreply@example.com',
            [user.email],
            fail_silently=False,
        )

        return redirect('confirm')


class ConfirmForm(FormView):
    model = Profile
    form_class = ConfirmationCodeForm
    template_name = 'registration/confirm_code.html'
    success_url = '/accounts/login/'
    context_object_name = 'profile'

    def form_valid(self, form):
        """ Получаем введенный в форму код методом .cleaned_data по полю code
            Фильтруем профиль по полю confirmation_code = code (полученный в форме)
            Далее проверка, если QuaerySet пустой, пишем ошибку в форму, либо в ином случае
            меняем у пользователя статус аккаунта на True """

        code = form.cleaned_data['code']
        profiles = Profile.objects.filter(confirmation_code=code)
        print('code from form:', code)
        print(profiles)
        if profiles.exists():
            user = profiles.first().user
            print(user)
            user.is_active = True
            user.save()
            return super().form_valid(form)
        else:
            form.add_error('code', 'Confirmation code is incorrect.')
            return self.form_invalid(form)
