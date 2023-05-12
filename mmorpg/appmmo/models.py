from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Advertisement(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    heading = models.CharField(max_length=128, help_text=('Название объявления'))
    text = models.TextField(help_text=('Это текст объявления'))
    dateCreation = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=64, help_text=('Это категория объявления'))
    postCategory = models.ForeignKey(Advertisement, related_name='postCategory', on_delete=models.CASCADE)

    def __str__(self):
        return self.name.title()


class Responses(models.Model):
    advertisement = models.ForeignKey(Advertisement, related_name='responses', on_delete=models.CASCADE)

    user = models.ForeignKey(User, related_name='respuser', on_delete=models.CASCADE)

    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
