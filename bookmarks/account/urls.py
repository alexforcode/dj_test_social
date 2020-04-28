from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views


app_name = 'account'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
