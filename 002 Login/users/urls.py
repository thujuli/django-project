from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginUser, name='login'),
    path('create-user/', views.createUser, name='create-user'),
    path('profile/', views.profileUser, name='profile'),
]
