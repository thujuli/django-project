from django.shortcuts import render
from .models import Post


def posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }

    return render(request, 'blogs/posts.html', context)


def detailPost(request, slugInput):
    post = Post.objects.get(slug=slugInput)
    context = {
        'post': post
    }

    return render(request, 'blogs/detail-post.html', context)
