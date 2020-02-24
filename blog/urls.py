from django.contrib import admin
from django.urls import path
from .views import *

app = 'blog'

urlpatterns = [
    path('', home_view),
    path('create/', create_new),
]
