import django_filters
from django.forms import DateInput
from django_filters import FilterSet, ChoiceFilter, ModelChoiceFilter
from .models import Advertisement


class AdvertisementFilter(FilterSet):
    added_after = django_filters.DateFilter(
        field_name='dateCreation',
        lookup_expr='gte',
        label='Дата',
        widget=DateInput(
            attrs={'type': 'date'},
        ),
    )

    rank = ChoiceFilter(
        field_name='classType',
        label='Тип персонажа:',
        choices=Advertisement.CATEGORY_CHOIESES
    )

    title_search = django_filters.CharFilter(
        field_name='heading',
        lookup_expr='icontains',
        label='Название объявления:',
    )


class AdvFilter(FilterSet):
    added_after = django_filters.DateFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label='Дата',
        widget=DateInput(
            attrs={'type': 'date'},
        ),
    )

    filtertitleBoard = ModelChoiceFilter(
        field_name='heading',
        queryset=Advertisement.objects.all(),
        label='Выберите статью',
        empty_label="--Заголовок--"
    )

    rank = ChoiceFilter(
        field_name='classType',
        label='Тип персонажа:',
        choices=Advertisement.CATEGORY_CHOIESES,
        empty_label="--Класс--"
    )
