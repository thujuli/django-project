from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    'class': 'bg-gray-200 mb-2 shadow-none  dark:bg-gray-800',
                    'placeholder': self.fields[field].label
                })


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    'class': 'bg-gray-200 mb-2 shadow-none  dark:bg-gray-800',
                    'placeholder': self.fields[field].label
                })


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = (
            'profile_image',
            'bio',
            'location',
        )
