from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView

urlpatterns = [
    path('account/login/', LoginView.as_view(template_name = 'sign/login.html'),name='login'),
    path('account/logout/', LogoutView.as_view(template_name = 'sign/logout.html'),name='logout'),
    path('account/signup/', BaseRegisterView.as_view(template_name = 'sign/signup.html'), name='signup'),
]

