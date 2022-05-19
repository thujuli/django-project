from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.

class LikePost(models.Model):
    post_id = models.CharField(max_length=255)
    username = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, unique=True, editable=False)
    user = models.CharField(max_length=255)
    image = models.ImageField(upload_to='feed_images')
    caption = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    total_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_user = models.IntegerField(editable=False)
    profile_image = models.ImageField(
        upload_to='profile_images/', default='default.jpg')
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username
