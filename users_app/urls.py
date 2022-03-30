from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('user/new', views.add_user),
]