from django.db import models
import uuid


class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(default='default.jpg', upload_to='book')
    genres = models.ManyToManyField(Genre, blank=True)
    published = models.CharField(max_length=255, null=True, blank=True)
    studio = models.CharField(max_length=255, null=True, blank=True)
    main_character = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.title
