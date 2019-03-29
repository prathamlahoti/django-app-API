from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    """ Post Model """
    title = models.CharField(unique=True, max_length=80)
    context = models.TextField()
    posted_date = models.DateField(default=timezone.now)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('tags.Tag')
    # post meta data
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

