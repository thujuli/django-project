from django.shortcuts import render
from blogs.models import Post


def index(request):
    posts = Post.objects.all()
    categories = Post.objects.values('category').distinct()
    context = {
        'posts': posts,
        'categories': categories
    }
    return render(request, 'index.html', context)
