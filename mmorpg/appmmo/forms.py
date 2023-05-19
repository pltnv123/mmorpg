from django import forms
from .models import Advertisement, Responses


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['heading', 'text', 'classType', 'image']


class ResponsesForm(forms.ModelForm):
    text = forms.CharField(
        label='Текст отклика',
        widget=forms.Textarea(),
        required=True
    )

    class Meta:
        model = Responses
        fields = ['text']
