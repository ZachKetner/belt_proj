from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('user/<int:userid>', views.userQuotes),
    path('delete/<int:userid>', views.delete),
    path('myaccount/<int:userid>', views.userProfile),
    path('edit/<int:userid>', views.update),
    path('like/<int:userid>', views.add_like),
]