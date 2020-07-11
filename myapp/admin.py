from django.contrib import admin

# Register your models here.
from .models import Notion, NotionLike


class NotionLikeAdmin(admin.TabularInline):
    model = NotionLike


class NotionAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user']
    search_fields = ['user__username', 'user__email']

    class Meta:
        model = Notion


admin.site.register(Notion, NotionAdmin)
