from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Profile
from .forms import CustomUserCreationForm

from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def signin(request):
    form = AuthenticationForm
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('signup')
        else:
            messages.info(
                request, 'You have entered an invalid username or password')
            return redirect('login')
    return render(request, 'signin.html', {'form': form})


def signup(request):
    form = CustomUserCreationForm
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username=username):
                messages.info(request, 'Username is Taken. Try another!')
                return redirect('signup')
            elif User.objects.filter(email=email):
                messages.info(request, 'Email is Taken. Try another!')
                return redirect('signup')
            else:
                # create user
                user = User.objects.create_user(
                    username=username, email=email, password=password1)
                user.save()

                # create new profile
                model_user = User.objects.filter(username=username)
                new_profile = Profile.objects.create(
                    user=model_user, id_user=model_user.id)
                new_profile.save()

                # authenticated & login
                user = authenticate(username=username, password=password1)
                if user is not None:
                    login(request, user)
                    return redirect('signup')  # change to settings url
                else:
                    messages.info(
                        request, 'Something went wrong please try again')
                    return redirect('login')  # change to login url

        else:
            messages.info(request, 'Password Not Match')
    return render(request, 'signup.html', {'form': form})
