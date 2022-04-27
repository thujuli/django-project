from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('book/<str:pk>/', views.readBook, name='read-book'),
    path('create-book/', views.createBook, name='create-book'),
    path('update-book/<str:pk>/', views.updateBook, name='update-book'),
    path('delete-book/<str:pk>/', views.deleteBook, name='delete-book'),
]
