import django_filters
from django.forms import DateInput
from django_filters import FilterSet, ChoiceFilter, ModelChoiceFilter, CharFilter
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

def ourBranches(request):
    if request is None:
        return Advertisement.objects.none()

    author = request.user
    return Advertisement.objects.filter(author=author)

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
        queryset=ourBranches,
        label='Выберите статью',
        empty_label="--Заголовок--"
    )

    rank = ChoiceFilter(
        field_name='classType',
        label='Тип персонажа:',
        choices=Advertisement.CATEGORY_CHOIESES,
        empty_label="--Класс--"
    )

