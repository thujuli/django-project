from django.shortcuts import render
from .models import Post


def categoryMap(request):
    posts = Post.objects.all()
    categories = Post.objects.values('category').distinct()
    context = {
        'posts': posts,
        'categories': categories
    }

    return render(request, 'snippets/category-map.html', context)


def posts(request):
    posts = Post.objects.all()
    categories = Post.objects.values('category').distinct()
    context = {
        'posts': posts,
        'categories': categories
    }

    return render(request, 'blogs/posts.html', context)


def categoryPost(request, categoryInput):
    posts = Post.objects.filter(category=categoryInput)
    categories = Post.objects.values('category').distinct()
    context = {
        'posts': posts,
        'categories': categories
    }

    return render(request, 'blogs/category-post.html', context)


def detailPost(request, slugInput):
    post = Post.objects.get(slug=slugInput)
    categories = Post.objects.values('category').distinct()
    context = {
        'posts': posts,
        'categories': categories
    }

    return render(request, 'blogs/detail-post.html', context)
