from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article
# Create your views here.


class ArticleCategoryListView(ListView):
    model = Article
    template_name = 'blogs/article-category_list.html'
    context_object_name = 'article_list'
    paginate_by = 3
    ordering = ['-published']

    def get_queryset(self, *args, **kwargs):
        self.queryset = self.model.objects.filter(
            category=self.kwargs['category'])
        return super().get_queryset(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        category_list = self.model.objects.values_list(
            'category', flat=True).distinct().exclude(category=self.kwargs['category'])
        self.kwargs.update({'category_list': category_list})
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)


class ArticleListView(ListView):
    model = Article
    template_name = 'blogs/article_list.html'
    context_object_name = 'article_list'
    paginate_by = 3
    ordering = ['-published']

    def get_context_data(self, *args, **kwargs):
        category_list = self.model.objects.values_list(
            'category', flat=True).distinct()
        self.kwargs.update({'category_list': category_list})
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blogs/article_detail.html'
    context_object_name = 'article'
