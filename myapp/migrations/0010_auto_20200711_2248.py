# Generated by Django 2.2.13 on 2020-07-11 22:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_remove_notion_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notion',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='notion_user', through='myapp.NotionLike', to=settings.AUTH_USER_MODEL),
        ),
    ]
