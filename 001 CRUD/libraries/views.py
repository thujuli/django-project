from django.shortcuts import render, redirect
from django.contrib import messages
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
            messages.success(request, 'Successfully Added a New Book')
            return redirect('home')
    else:
        form = BookForm()
        context = {
            'form': form
        }

    return render(request, 'libraries/create_update-book.html', context)


def updateBook(request, pk):
    book = Book.objects.get(id=pk)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updating the Book')
            return redirect('home')
    else:
        form = BookForm(instance=book)
        context = {
            'form': form,
            'book': book
        }

    return render(request, 'libraries/create_update-book.html', context)
