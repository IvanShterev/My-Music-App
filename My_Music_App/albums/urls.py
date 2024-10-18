from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_album, name='add-album'),
    path('<int:pk>/details', views.details_album, name='album-details'),
    path('<int:pk>/edit', views.edit_album, name='album-edit'),
    path('<int:pk>/delete', views.delete_album, name='album-delete')
]