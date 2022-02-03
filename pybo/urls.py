from django.urls import path

from . import views

urlpatterns = [
    path('pybo/', views.pybo),
]