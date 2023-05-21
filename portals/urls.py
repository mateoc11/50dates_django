from django.urls import path
from . import views

urlpatterns = [
    path('', views.portals, name='portals'),
    path('search/', views.searchPhotos, name='search'),
    path('photos/<int:userid>', views.redirectPhotos, name='photos'),
    path('photos/photoUpload/', views.photoUpload, name='photoUpload')
]