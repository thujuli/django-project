from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('settings/', views.settings, name='settings'),
]
