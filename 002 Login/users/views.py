from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm


def home(request):
    return render(request, 'users/home.html')


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # try:
        #     user = User.objects.get(username=username)
        # except:
        #     messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')

    return render(request, 'users/login-user.html')


@login_required(login_url='login')
def createUser(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
        context = {'form': form}
    return render(request, 'users/create-user.html', context)


@login_required(login_url='login')
def profileUser(request):
    context = {}
    return render(request, 'users/profile.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')
