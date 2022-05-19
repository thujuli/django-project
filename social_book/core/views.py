from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile, Post, LikePost
from .forms import CustomUserCreationForm, ProfileForm, PostForm
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


@login_required(login_url='login')
def index(request):
    form = PostForm
    user_post = Post.objects.filter(user=request.user.username)

    context = {
        'form': form,
        'user_post': user_post
    }
    return render(request, 'index.html', context)


@login_required(login_url='login')
def profile(request, pk):
    user_object = User.objects.get(username=pk)
    profile = Profile.objects.get(user=user_object)
    user_post = Post.objects.filter(user=pk)
    user_post_length = len(user_post)

    context = {
        'profile': profile,
        'user_post': user_post,
        'user_post_length': user_post_length,

    }
    return render(request, 'profile.html', context)


@login_required(login_url='login')
def likePost(request):
    # get data for models LikePost
    post_id = request.GET.get('post_id')
    username = request.user.username

    # get models for update data total_likes
    post = Post.objects.get(id=post_id)

    # select table in models LikePost to update logic
    like_filter = LikePost.objects.filter(
        post_id=post_id, username=username).first()

    # update logic total_likes in Post
    if like_filter is None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.total_likes += 1
        post.save()
        return redirect('index')

    else:
        like_filter.delete()
        post.total_likes -= 1
        post.save()
        return redirect('index')


@login_required(login_url='login')
def upload(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        image = request.FILES.get('image')
        caption = request.POST.get('caption')
        user = request.user.username

        if form.is_valid():
            new_post = Post.objects.create(
                user=user, image=image, caption=caption)
            new_post.save()
            return redirect('index')
    else:
        return redirect('index')


@login_required(login_url='login')
def setting(request):
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

        return redirect('index')

    context = {
        'form': form,
        'user_profile': user_profile,
    }
    return render(request, 'setting.html', context)


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
