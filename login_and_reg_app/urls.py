from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration),
    path('register', views.register),
    path('login', views.login),
    path('log_out', views.log_out),
]