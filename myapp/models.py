from django.db import models
from django.conf import settings
import random

# Create your models here.
User = settings.AUTH_USER_MODEL


class Notion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # many
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='image/', blank=True, null=True)

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
