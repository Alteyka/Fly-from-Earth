from django.urls import path
from .views import *

urlpatterns = [
    path('cards_list/', cards_list, name='cards_list_url'),
    path('card/create/', CardCreate.as_view(), name='card_create_url'),
    path('card/<str:slug>/', CardDetail.as_view(), name='card_detail_url'),
    path('', start_page, name='start_page_url'),
    path('random_card/', random_card, name='random_card_url'),
    path('card/<str:slug>/update/', CardUpdate.as_view(), name='card_update_url'),
    path('card/<str:slug>/delete/', CardDelete.as_view(), name='card_delete_url'),
    path('login/', login_view, name='login_view_url'),
    path('logout/', logout_view, name='logout_view_url'),
    path('password_reset/', password_reset, name='password_reset'),
    path('register/', register_view, name='register_view_url'),
]
