from django.db import models
from django.conf import settings
import random

# Create your models here.
User = settings.AUTH_USER_MODEL


class NotionLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notion = models.ForeignKey("Notion", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class Notion(models.Model):
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # many
    content = models.TextField(blank=True, null=True)
    likes = models.ManyToManyField(
        User, related_name='notion_user', blank=True, through=NotionLike)
    image = models.FileField(upload_to='image/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.content

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 200)
        }
