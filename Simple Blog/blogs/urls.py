from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCategoryListView,
    ArticleCreateFormView,
    ArticleManageListView,
    ArticleDeleteView,
    ArticleUpdateFormView
)

app_name = 'blogs'

urlpatterns = [
    path('manage/update/<int:pk>/', ArticleUpdateFormView.as_view(), name='update'),
    path('manage/delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete'),
    path('manage/', ArticleManageListView.as_view(), name='manage'),
    path('<str:category>/<int:page>/',
         ArticleCategoryListView.as_view(), name='category'),
    path('detail/<slug:slug>/', ArticleDetailView.as_view(), name='detail'),
    path('create/', ArticleCreateFormView.as_view(), name='create'),
    path('<int:page>/', ArticleListView.as_view(), name='list'),
]
