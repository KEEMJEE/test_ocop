from django.urls import path
from . import views

app_name = "point"

urlpatterns = [
    path('createcarbon/', views.Createcarbon, name='createcarbon'),
    path('creategreen/', views.Creategreen, name='creategreen'),
    path('carbonlist/', views.Carbonlist, name='carbonlist'),
    path('greenlist/', views.Greenlist, name='greenlist'),
    path('carbonlist/modify/', views.Carbon_Modify, name='carbonmodify'),
    path('carbon/', views.Carbonpage, name='carbonpage'),
    path('green/', views.Greenpage, name='greenpage'),
]