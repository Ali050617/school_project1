from django.urls import path
from . import views

app_name = 'travel'

urlpatterns = [
    path('list/', views.travel_list, name='travel'),
    path('create/', views.travel_create, name='create'),
    path('detail/<int:pk>', views.travel_detail, name='detail'),
    path('update/<int:pk>', views.travel_update, name='update'),
    path('delete/<int:pk>', views.travel_delete, name='delete')
]