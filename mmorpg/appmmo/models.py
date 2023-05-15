from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Advertisement(models.Model):
    tank = 'TK'
    heal = 'HL'
    dd = 'DD'
    trader = 'TD'
    guild_masters = 'GM'
    quest_giver = 'KG'
    blacksmith = 'BS'
    the_tanner = 'TR'
    potions_master = 'PM'
    master_of_spells = 'SP'

    CATEGORY_CHOIESES = (
        (tank, ('Танки')),
        (heal, ('Хилы')),
        (dd, ('ДД')),
        (trader, ('Торговец')),
        (guild_masters, ('Гилдмастер')),
        (quest_giver, ('Квестгивер')),
        (blacksmith, ('Кузнец')),
        (the_tanner, ('Кожевник')),
        (potions_master, ('Зельевар')),
        (master_of_spells, ('Мастер заклинаний')),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=128, help_text=('Название объявления'))
    text = models.TextField(help_text=('Это текст объявления'))
    classType = models.CharField(max_length=2, choices=CATEGORY_CHOIESES, help_text=('Тип класса'))
    dateCreation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.heading}: {self.text}. Автор: {self.author}, тип героя: {self.classType}'


class Responses(models.Model):
    advertisement = models.ForeignKey(Advertisement, related_name='responses', on_delete=models.CASCADE)

    user = models.ForeignKey(User, related_name='respuser', on_delete=models.CASCADE)

    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
