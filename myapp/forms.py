from django.conf import settings
from django import forms
from .models import Notion


MAX_NOTION_LENGTH = settings.MAX_NOTION_LENGTH


class NotionForm(forms.ModelForm):

    class Meta:
        model = Notion
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_NOTION_LENGTH:
            raise forms.ValidationError("This notion is too long")
        return content
