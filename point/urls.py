from django.urls import path
from . import views

app_name = "point"

urlpatterns = [
    path('createcarbon/', views.Createcarbon, name='createcarbon'),
    path('creategreen/', views.Creategreen, name='creategreen'),
    path('carbonlist/', views.Carbonlist, name='carbonlist'),
    path('greenlist/', views.Greenlist, name='greenlist'),
    path('carbonlist/modify/<int:Carbonpoint_id>/', views.Carbon_Modify, name='carbonmodify'),
    path('greenlist/modify/<int:Greenpoint_id>/', views.Green_Modify, name='greenmodify'),
    path('carbonlist/delete/<int:Carbonpoint_id>/', views.Carbon_Delete, name='carbondelete'),
    path('greenlist/delete/<int:Greenpoint_id>/', views.Green_Delete, name='greendelete'),
    path('carbon/', views.Carbonpage, name='carbonpage'),
    path('green/', views.Greenpage, name='greenpage'),
]