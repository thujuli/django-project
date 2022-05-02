from django.urls import path
from . import views


urlpatterns = [
    path('', views.posts, name='posts'),
    path('<slug:slugInput>/', views.detailPost, name='detail-post'),
    path('category/<str:categoryInput>/',
         views.categoryPost, name='category-post'),
]
