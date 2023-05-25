from celery import shared_task
import time
import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Advertisement


@shared_task
def email_every_monday():
    """
    Отправляет еженедельный дайджест публикаций пользователям.

        Функция получает все объявления, созданные за последнюю неделю, и отправляет их
        в виде дайджеста на электронную почту каждому зарегистрированному пользователю.
    """

    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    adver = Advertisement.objects.filter(dateCreation__gte=last_week)
    users = set(User.objects.all().values_list('email', flat=True))
    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'adver': adver,
        }
    )

    for email in users:
        send_mail(
            subject='Публикации за неделю',
            message='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            html_message=html_content,
        )
