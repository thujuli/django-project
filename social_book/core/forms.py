from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile


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
