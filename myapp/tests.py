from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Notion
# Create your tests here.

User = get_user_model()


class NotionTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="cfe", password="somepassword")

    def test_notion_created(self):
        notion_obj = Notion.objects.create(content="MyNotion", user=self.user)
        self.assertEqual(notion_obj.id, 1)
        self.assertEqual(notion_obj.user, self.user)
