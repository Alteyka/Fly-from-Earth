from django.shortcuts import render
from django.urls import path

from .views import *

urlpatterns = [
    path('', cards_list, name='cards_list_url'),
    path('card/<str:slug>/', CardDetail.as_view(), name='card_detail_url')
]
