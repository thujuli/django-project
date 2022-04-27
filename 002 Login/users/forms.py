from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    model = UserCreationForm
    fields = '__all__'
