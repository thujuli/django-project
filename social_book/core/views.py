from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


@login_required(login_url='login')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)
    form = ProfileForm(instance=user_profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,
                           instance=user_profile)

        # handling image from user upload (None)
        if request.FILES.get('profile_image') == None:
            profile_image = user_profile.profile_image

        # handling image from user when uploaded
        if request.FILES.get('profile_image') != None:
            profile_image = request.FILES.get('profile_image')

        bio = request.POST.get('bio')
        location = request.POST.get('location')
        if form.is_valid():
            user_profile.profile_image = profile_image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()

        return redirect('settings')  # index view

    context = {
        'form': form,
        'user_profile': user_profile,
    }
    return render(request, 'settings.html', context)


@login_required(login_url='login')
def logoutView(request):
    logout(request)
    return redirect('login')


def signin(request):
    if request.user.is_authenticated:
        return redirect('settings')

    form = AuthenticationForm
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('settings')
        else:
            messages.info(
                request, 'You have entered an invalid username or password')
            return redirect('login')
    return render(request, 'signin.html', {'form': form})


def signup(request):
    if request.user.is_authenticated:
        return redirect('settings')

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
                    return redirect('settings')
                else:
                    messages.info(
                        request, 'Something went wrong please try again')
                    return redirect('login')

        else:
            messages.info(request, 'Password Not Match')
    return render(request, 'signup.html', {'form': form})
