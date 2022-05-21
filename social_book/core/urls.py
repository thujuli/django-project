from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('follow/', views.follow, name='follow'),
    path('like-post/', views.likePost, name='like-post'),
    path('upload/', views.upload, name='upload'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('setting/', views.setting, name='setting'),
    path('profile/<str:pk>/', views.profile, name='profile')
]
