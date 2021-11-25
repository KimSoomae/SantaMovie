from django.db import models
from django.conf import settings
# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Community(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, related_name='user_community')
    tags = models.ManyToManyField(Tag, related_name="communities", blank=True)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='comments', blank=True)
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

