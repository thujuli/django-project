from django.urls import path
from .views import ArticleListView, ArticleDetailView

app_name = 'blogs'

urlpatterns = [
    path('detail/<slug:slug>/', ArticleDetailView.as_view(), name='detail'),
    path('<str:page>/', ArticleListView.as_view(), name='list'),
]
