from django.urls import path

from .views import AdvertisementView, CreateAdvertisement, UpgradeAdvertisement, DeleteAdvertisement, ProfileView,\
    AdvertisementDetailView

urlpatterns = [
    path('', AdvertisementView.as_view(), name='advertisement'),
    path('<int:pk>/', AdvertisementDetailView.as_view(), name='advertisement_detail'),
    path('create/', CreateAdvertisement.as_view(), name='advertisement_create'),
    path('<int:pk>/update/', UpgradeAdvertisement.as_view(), name='advertisement_upgrade'),
    path('<int:pk>/delete/', DeleteAdvertisement.as_view(), name='advertisement_delete'),
    path('profile/', ProfileView.as_view(), name='profile'),
]