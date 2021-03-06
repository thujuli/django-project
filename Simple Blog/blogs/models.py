from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.title)
        super().save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        url_slug = {'slug': self.slug}
        return reverse('blogs:detail', kwargs=url_slug)
