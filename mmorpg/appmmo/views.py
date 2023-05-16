from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from .filters import PostFilter
from .models import Advertisement, Responses


# Create your views here.
class AdvertisementView(ListView):
    model = Advertisement
    template_name = 'Advertisement.html'
    context_object_name = 'advertisements'
    paginate_by = 10
    ordering = ['-dateCreation']


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)

        return self.filterset.qs


class AdvertisementDetailView(DetailView):
    model = Advertisement
    template_name = 'AdPk.html'
    context_object_name = 'Adver'


class CreateAdvertisement(CreateView):  # PermissionRequiredMixin

    def get(self, request):
        return render(request, 'CreateAdvertisement.html')


class UpgradeAdvertisement(CreateView):
    def get(self, request):
        return render(request, 'UpgradeAdvertisement.html')


class DeleteAdvertisement(CreateView):
    def get(self, request):
        return render(request, 'DeleteAdvertisement.html')

class ProfileView(CreateView):
    def get(self, request):
        return render(request, 'Profile.html')