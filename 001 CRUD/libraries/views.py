from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


def index(request):
    listBook = Book.objects.all()
    context = {
        'listBook': listBook
    }
    return render(request, 'libraries/home.html', context)


def readBook(request, pk):
    book = Book.objects.get(id=pk)
    context = {
        'book': book
    }
    return render(request, 'libraries/read-book.html', context)


def createBook(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
        context = {
            'form': form
        }

    return render(request, 'libraries/create-book.html', context)
