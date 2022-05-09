from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCategoryListView

app_name = 'blogs'

urlpatterns = [
    path('<str:category>/<int:page>/',
         ArticleCategoryListView.as_view(), name='category'),
    path('detail/<slug:slug>/', ArticleDetailView.as_view(), name='detail'),
    path('<int:page>/', ArticleListView.as_view(), name='list'),
]
