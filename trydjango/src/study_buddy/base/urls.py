from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name = "home" ),
    path('room/<str:pk>', views.room_view, name = 'room'),
    path('create-room/', views.create_room,name="create-room"),
    path('update-room/<str:pk>/', views.update_room, name="update-room"),
    path('delete-room/<str:pk>/', views.delete_room, name="delete-room"),
]
