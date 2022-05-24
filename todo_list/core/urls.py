from django.urls import path
from . import views

urlpatterns = [
    path('delete/<int:pk>', views.delete, name='delete'),
    path('update/<int:pk>', views.update, name='update'),
    path('done/', views.done, name='done'),
    path('pending/', views.pending, name='pending'),
    path('delete-all/', views.deleteAll, name='delete_all'),
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
]
