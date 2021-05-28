from django.contrib import admin
from django.urls import path

from petstagram.common import views

urlpatterns = [
    path('', views.landing_page, name='landing')
]
