from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView, upgrade_me, IndexView

urlpatterns = [
    path('login/',
         LoginView.as_view(template_name = 'signup/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name = 'signup/logout.html'),
         name='logout'),
    path('signup/',
         BaseRegisterView.as_view(template_name = 'signup/signup.html'),
         name='signup'),
    path('upgrade/', upgrade_me, name = 'upgrade'),
    path('ac/', IndexView.as_view(template_name='signup/index.html')),
]