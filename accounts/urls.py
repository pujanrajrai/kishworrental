from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.user_registration, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('welcomepage/', views.welcomepage, name='welcomepage')
]
