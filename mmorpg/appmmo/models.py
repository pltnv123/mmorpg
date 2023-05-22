from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.author.id, filename)


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
    image = models.ImageField(max_length=255,  upload_to=user_directory_path, null=True, blank=True)
    dateCreation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.heading}'

    def get_absolute_url(self):
        return reverse('advertisement_detail', args=[str(self.id), ])

class Responses(models.Model):
    advertisement = models.ForeignKey(Advertisement, related_name='responses', on_delete=models.CASCADE)

    user = models.ForeignKey(User, related_name='respuser', on_delete=models.CASCADE)

    text = models.TextField(help_text=('Поле отклика'))
    dateCreation = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

