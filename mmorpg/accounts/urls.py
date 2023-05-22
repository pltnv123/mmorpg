from django.urls import path
from .views import SignUp, ConfirmForm

urlpatterns = [
    path('signup', SignUp.as_view(), name='signup'),
    path('confirm', ConfirmForm.as_view(), name='confirm'),
]