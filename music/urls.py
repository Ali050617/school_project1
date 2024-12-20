from django.urls import path

from . import views

app_name = 'music'

urlpatterns = [
    path('list/', views.music_list, name='music'),
    path('create/', views.music_create, name='create'),
    path('detail/<int:pk>/', views.music_detail, name='detail'),
    path('update/<int:pk>/', views.music_update, name='update'),
    path('delete/<int:pk>/', views.music_delete, name='delete'),
]