from django.urls import path
from . import views

app_name = 'vehicle'
urlpatterns = [
    path('add/', views.add_vehicle, name='add_vehicle'),
]
