from django.urls import path
from .views import AdvertisementView, CreateAdvertisement, UpdateAdvertisement, DeleteAdvertisement, ProfileView, \
    AdvertisementDetailView, ResponseCreateView, DeleteResponses, ResponsesDetailView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', AdvertisementView.as_view(), name='advertisement'),
                  path('<int:pk>/', AdvertisementDetailView.as_view(), name='advertisement_detail'),
                  path('create/', CreateAdvertisement.as_view(), name='advertisement_create'),
                  path('<int:pk>/update/', UpdateAdvertisement.as_view(), name='advertisement_update'),
                  path('<int:pk>/delete/', DeleteAdvertisement.as_view(), name='advertisement_delete'),
                  path('profile/', ProfileView.as_view(), name='profile'),

                  path('<int:pk>/response_create/', ResponseCreateView.as_view(), name='response_create'),
                  path('<int:pk>/<int:pk_res>/', ResponsesDetailView.as_view(), name='responses_detail'),
                  path('<int:pk>/<int:pk_res>/response_delete/', DeleteResponses.as_view(), name='response_delete'),

                  # path('responses/<int:pk>/', ResponseDetailView.as_view(), name='response_detail'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
