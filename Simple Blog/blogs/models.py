from django.utils.text import slugify
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    category = models.CharField(max_length=255)
    slug = models.SlugField(editable=False, blank=True)
    publish = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()

    def __str__(self):
        return self.title
