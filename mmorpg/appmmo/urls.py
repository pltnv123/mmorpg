from django.urls import path
from .views import AdvertisementView, CreateAdvertisement, UpdateAdvertisement, DeleteAdvertisement, ProfileView,\
    AdvertisementDetailView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', AdvertisementView.as_view(), name='advertisement'),
    path('<int:pk>/', AdvertisementDetailView.as_view(), name='advertisement_detail'),
    path('create/', CreateAdvertisement.as_view(), name='advertisement_create'),
    path('<int:pk>/update/', UpdateAdvertisement.as_view(), name='advertisement_udate'),
    path('<int:pk>/delete/', DeleteAdvertisement.as_view(), name='advertisement_delete'),
    path('profile/', ProfileView.as_view(), name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)