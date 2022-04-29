from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    featured_image = models.ImageField(
        default='user-default.png', upload_to='profile/')
    short_desc = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)
