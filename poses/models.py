from django.db import models

from django.contrib.auth.models import User


LEVEL_CHOICES = [
    ('beginner', 'Beginner'),
    ('advanced', 'Advanced'),
    ('intermediate', 'Intermediate'),
]


class Pose(models.Model):

    name = models.CharField(max_length=300)
    description = models.TextField(max_length=3000, null=True, blank=True)

    level = models.CharField (max_length=13, choices=LEVEL_CHOICES)

    image = models.ImageField(upload_to='upload/', default="")

    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url