from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Article
from .forms import ArticleForm
# Create your views here.


class ArticleUpdateFormView(UpdateView):
    template_name = 'blogs/article-update_form.html'
    model = Article
    form_class = ArticleForm


class ArticleDeleteView(DeleteView):
    template_name = 'blogs/article_confirm_delete.html'
    model = Article
    success_url = reverse_lazy('blogs:manage')


class ArticleManageListView(ListView):
    model = Article
    template_name = 'blogs/article-manage_list.html'
    context_object_name = 'article_list'
    ordering = ['-published']


class ArticleCreateFormView(CreateView):
    template_name = 'blogs/article-create_form.html'
    form_class = ArticleForm


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

    def get_context_data(self, *args, **kwargs):
        related_article = self.model.objects.filter(
            category=self.object.category).exclude(id=self.object.id).order_by('-published')[:2]
        self.kwargs.update({'related_article': related_article})
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)
