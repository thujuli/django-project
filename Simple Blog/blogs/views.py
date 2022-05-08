from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article
# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = 'blogs/article_list.html'
    context_object_name = 'article_list'
    paginate_by = 3
    ordering = ['-published']


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blogs/article_detail.html'
    context_object_name = 'article'
