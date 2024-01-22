from api.views import index
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('index/',index),
]
