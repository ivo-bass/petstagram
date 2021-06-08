from django.contrib import admin
from django.urls import path, include

from petstagram.pets.views import pet_all, pet_detail, pet_like

urlpatterns = [
    path("", pet_all, name='pet all'),
    path("details/<int:pk>", pet_detail, name='pet detail'),
    path("like/<int:pk>", pet_like, name='pet like'),
]
