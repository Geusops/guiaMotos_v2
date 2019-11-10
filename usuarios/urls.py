from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^cadastra$',  views.RegistrarUsuarioView.as_view(), name='cadastrar')
]