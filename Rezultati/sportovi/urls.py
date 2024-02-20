from django.urls import path
from .views import *

app_name = 'sportovi'

urlpatterns = [
    path('', homepage, name='homepage'),

    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('logout/', user_logout, name='logout'),

    path('sportovi/', SportoviListView.as_view(), name='sportovi_list'),
    path('sportovi/create/', CreateSport.as_view(), name='create_sport'),
    path('sportovi/update/<int:pk>/', UpdateSport.as_view(), name='update_sport'),
    path('sportovi/delete/<int:pk>/', DeleteSport.as_view(), name='delete_sport'),

    path('natjecanje/', NatjecanjeListView.as_view(), name='natjecanje_list'),
    path('natjecanje/<int:sport_pk>/', NatjecanjeListView.as_view(), name='natjecanje_list'),
    path('natjecanje/create/', CreateNatjecanje.as_view(), name='create_natjecanje'),
    path('natjecanje/update/<int:pk>/', UpdateNatjecanje.as_view(), name='update_natjecanje'),
    path('natjecanje/delete/<int:pk>/', DeleteNatjecanje.as_view(), name='delete_natjecanje'),

    path('timovi/', TimListView.as_view(), name='tim_list'),
    path('timovi/<int:natjecanje_pk>/', TimListView.as_view(), name='tim_list'),
    path('timovi/create/', CreateTim.as_view(), name='create_tim'),
    path('timovi/update/<int:pk>/', UpdateTim.as_view(), name='update_tim'),
    path('timovi/delete/<int:pk>/', DeleteTim.as_view(), name='delete_tim'),

    path('rezultati/', RezultatUtakmiceListView.as_view(), name='rezultati_timova'),
    path('rezultati/tim/<int:tim_pk>/', RezultatUtakmiceListView.as_view(), name='rezultati_timova'),
    path('rezultati/create/', CreateUtakmica.as_view(), name='create_utakmica'),
    path('rezultati/update/<int:pk>/', UpdateUtakmica.as_view(), name='update_utakmica'),
    path('rezultati/delete/<int:pk>/', DeleteUtakimca.as_view(), name='delete_utakmica'),
]