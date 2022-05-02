from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-project/', views.createPoject, name='create-project'),
]
