from django.contrib.auth.views import LoginView
from django.urls import path
from .views import SignUp, ConfirmForm

urlpatterns = [
    path('signup', SignUp.as_view(), name='signup'),
    path('confirm', ConfirmForm.as_view(), name='confirm'),
    path('accounts/login/', LoginView.as_view(), name='login'),
]