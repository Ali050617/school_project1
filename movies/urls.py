from django.urls import path

from . import views

app_name = 'movies'

urlpatterns = [
    path('list/', views.movies_list, name='list'),
    path('create/', views.movies_create, name='create'),
    path('detail/<int:pk>/', views.movies_detail, name='detail'),
    path('update/<int:pk>/', views.movies_update, name='update'),
    path('delete/<int:pk>/', views.movies_delete, name='delete'),

]