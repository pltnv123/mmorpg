from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .filters import PostFilter
from .models import Advertisement, Responses
from .forms import AdvertisementForm


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
    template_name = 'AdvertisementPk.html'
    context_object_name = 'Adver'


class CreateAdvertisement(CreateView):  # PermissionRequiredMixin

    form_class = AdvertisementForm
    model = Advertisement
    template_name = 'CreateAdvertisement.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        print(form.instance.author)
        return super().form_valid(form)


class UpdateAdvertisement(UpdateView):
    form_class = AdvertisementForm
    model = Advertisement
    template_name = 'UpdateAdvertisement.html'


class DeleteAdvertisement(DeleteView):
    model = Advertisement
    template_name = 'DeleteAdvertisement.html'
    success_url = reverse_lazy('advertisement')


class ProfileView(CreateView):
    def get(self, request):
        return render(request, 'Profile.html')
