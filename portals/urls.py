from django.urls import path
from . import views

urlpatterns = [
    path('', views.portals, name='portals'),
    path('search/', views.searchPhotos, name='search')
]