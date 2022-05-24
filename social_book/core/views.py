from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile, Post, LikePost, FollowCount
from .forms import CustomUserCreationForm, ProfileForm, PostForm, SearchPeopleForm, UserLoginForm
from itertools import chain
import random

# Create your views here.


@login_required(login_url='login')
def index(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    post_form = PostForm
    search_form = SearchPeopleForm
    user_following_list = []
    feed = []

    # get following list
    following_list = FollowCount.objects.filter(follower=request.user.username)
    for users in following_list:
        user_following_list.append(users.user)

    # get feed list
    for username in user_following_list:
        feed_list = Post.objects.filter(user=username)
        feed.append(feed_list)

    # list a objects
    feed_list = list(chain(*feed))

    # new suggestions list start
    all_users = User.objects.all()
    user_following_all = []

    for user in following_list:
        user_list = User.objects.get(username=user.user)
        user_following_all.append(user_list)

    new_suggestion_list = [
        x for x in all_users if (x not in user_following_all)]
    current_user = User.objects.filter(username=request.user.username)
    final_suggestions_list = [
        x for x in new_suggestion_list if (x not in current_user)]
    random.shuffle(final_suggestions_list)

    profile_list = []
    profile_list_all = []

    for users in final_suggestions_list:
        profile_list.append(users.id)

    for ids in profile_list:
        user = Profile.objects.filter(id_user=ids)
        profile_list_all.append(user)

    suggestions_profile_list = list(chain(*profile_list_all))

    context = {
        'user_profile': user_profile,
        'search_form': search_form,
        'post_form': post_form,
        'user_post': feed_list,
        'suggestions_profile_list': suggestions_profile_list[0:3],
    }
    return render(request, 'index.html', context)


@login_required(login_url='login')
def search(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    search_form = SearchPeopleForm

    if request.method == 'POST':
        search_user = request.POST.get('search')
        username_profile = User.objects.filter(username__icontains=search_user)
        username_list = []
        profile = []

        for usernames in username_profile:
            username_list.append(usernames)

        for profiles in username_list:
            profile_lists = Profile.objects.filter(user=profiles)
            profile.append(profile_lists)

        profile_list = list(chain(*profile))

    context = {
        'search_user': search_user,
        'profile_list': profile_list,
        'search_form': search_form,
        'user_profile': user_profile,
    }
    return render(request, 'search.html', context)


@login_required(login_url='login')
def profile(request, pk):
    user_object = User.objects.get(username=pk)
    profile = Profile.objects.get(user=user_object)
    user_post = Post.objects.filter(user=pk)
    user_post_length = len(user_post)

    follower = request.user.username
    user = pk

    if FollowCount.objects.filter(follower=follower, user=user):
        button_text = 'Unfollow'
    else:
        button_text = 'Follow'

    user_followers = len(FollowCount.objects.filter(user=pk))
    user_following = len(FollowCount.objects.filter(follower=pk))

    context = {
        'user_object': user_object,
        'profile': profile,
        'user_post': user_post,
        'user_post_length': user_post_length,
        'user_followers': user_followers,
        'user_following': user_following,
        'button_text': button_text,

    }
    return render(request, 'profile.html', context)


@login_required(login_url='login')
def follow(request):

    if request.method == 'POST':
        follower = request.POST.get('follower')
        user = request.POST.get('user')
        follower_filter = FollowCount.objects.filter(
            follower=follower, user=user).first()

        if follower_filter == None:
            new_follower = FollowCount.objects.create(
                follower=follower, user=user)
            new_follower.save()
            return redirect(reverse('profile', kwargs={'pk': user}))
        else:
            follower_filter.delete()
            return redirect(reverse('profile', kwargs={'pk': user}))
            # return redirect('profile'+user)

    return redirect('index')


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
        'profile_form': form,
        'user_profile': user_profile,
    }
    return render(request, 'setting.html', context)


@login_required(login_url='login')
def logoutView(request):
    logout(request)
    return redirect('login')


def signin(request):
    if request.user.is_authenticated:
        return redirect('setting')

    form = UserLoginForm(request.POST or None)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('setting')
        else:
            messages.info(
                request, 'You have entered an invalid username or password')
            return redirect('login')
    return render(request, 'signin.html', {'login_form': form})


def signup(request):
    if request.user.is_authenticated:
        return redirect('setting')

    signup_form = CustomUserCreationForm(request.POST or None)
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
                if signup_form.is_valid():
                    # create user
                    user = User.objects.create_user(
                        username=username, email=email, password=password1)
                    user.save()

                    # create new profile
                    model_user = User.objects.get(username=username)
                    new_profile = Profile.objects.create(
                        user=model_user, id_user=model_user.id)
                    new_profile.save()

                    # authenticated & login
                    user = authenticate(username=username, password=password1)
                    if user is not None:
                        login(request, user)
                        return redirect('setting')
                else:
                    messages.info(
                        request, "Oops, something went wrong, please try a new password that doesn't match your other personal information")
        else:
            messages.info(request, 'Password Not Match')
    return render(request, 'signup.html', {'signup_form': signup_form})
