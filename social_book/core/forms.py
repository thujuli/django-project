from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import Profile, Post


class SearchPeopleForm(forms.Form):
    search = forms.CharField(max_length=255)


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = (
            'image',
            'caption',
        )


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = (
            'profile_image',
            'bio',
            'location',
        )
