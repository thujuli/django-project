from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomUserCreationForm
# Create your views here.


def Signup(request):
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
                model_user = User.objects.create_user(
                    username=username, password=password1)
                new_user = Profile.objects.create(
                    user=model_user, id_user=model_user.id)

                # redirect to settings
                # authenticated & login
        else:
            messages.info(request, 'Password Not Match')
    return render(request, 'signup.html', {'form': form})
