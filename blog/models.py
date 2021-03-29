from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
#one user can have multiple posts

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User ,on_delete=models.CASCADE)
    # we are telling django that if the user is deleted the post shud also be deleted but vice versa shudnt happen

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})