from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Advertisement, Responses


# Create your views here.
class AdvertisementView(ListView):
    def get(self, request):
        return render(request, 'Advertisement.html')


class ProfileView(ListView):
    def get(self, request):
        return render(request, 'Profile.html')


class CreateAdvertisement(CreateView):  # PermissionRequiredMixin

    def get(self, request):
        return render(request, 'CreateAdvertisement.html')


class UpgradeAdvertisement(CreateView):
    def get(self, request):
        return render(request, 'UpgradeAdvertisement.html')


class DeleteAdvertisement(CreateView):
    def get(self, request):
        return render(request, 'DeleteAdvertisement.html')
