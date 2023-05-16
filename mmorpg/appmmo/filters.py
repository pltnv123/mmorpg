import django_filters
from django.forms import DateInput
from django_filters import FilterSet, ChoiceFilter
from .models import Advertisement


class PostFilter(FilterSet):
    added_after = django_filters.DateFilter(
        field_name='dateCreation',
        lookup_expr='gt',
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
        field_name='title',
        lookup_expr='icontains',
        label='Поиск по объявлениям:',
    )
