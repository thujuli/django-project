from django.db import models
import uuid


class Project(models.Model):
    title = models.CharField(max_length=255)
    featured_image = models.ImageField(
        upload_to='projects/', default='projects/default.jpg', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.title
