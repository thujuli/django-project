from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo

# Create your views here.


def pending(request):
    items = Todo.objects.filter(status=False)
    return render(request, 'index.html', {'items': items})


def done(request):
    items = Todo.objects.filter(status=True)
    return render(request, 'index.html', {'items': items})


def deleteAll(request):
    todo = Todo.objects.all()
    todo.delete()
    return redirect('index')


def create(request):
    create_form = TodoForm(request.POST or None)

    if request.method == 'POST':
        title = request.POST.get('title')
        if create_form.is_valid():
            todo = Todo.objects.create(title=title)
            todo.save()
            return redirect('index')
    else:
        return redirect('index')


def update(request, pk):
    if request.method == 'POST':
        todo = Todo.objects.get(id=pk)
        todo.status = not todo.status
        todo.save()

    return redirect('index')


def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('index')


def index(request):
    items = Todo.objects.all()
    create_form = TodoForm

    context = {
        'create_form': create_form,
        'items': items
    }
    return render(request, 'index.html', context)
