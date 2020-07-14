from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from .models import Notion
# Create your tests here.

User = get_user_model()


class NotionTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="cfe", password="somepassword")
        self.userb = User.objects.create_user(
            username="cfe2", password="somepassword2")
        Notion.objects.create(content="MyFirstNotion", user=self.user)
        Notion.objects.create(content="MySecondNotion", user=self.user)
        Notion.objects.create(content="MyThirdNotion", user=self.userb)
        self.currentCount = Notion.objects.all().count()

    def test_notion_created(self):
        notion_obj = Notion.objects.create(
            content="MyFourthNotion", user=self.user)
        self.assertEqual(notion_obj.id, 4)
        self.assertEqual(notion_obj.user, self.user)

    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password="somepassword")
        return client

    def test_notion_list(self):
        client = self.get_client()
        response = client.get("/api/notions/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_notion_list(self):
        client = self.get_client()
        response = client.get("/api/notions/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)

    def test_action_like(self):
        client = self.get_client()
        response = client.post("/api/notions/action/",
                               {"id": 1, "action": "like"})
        self.assertEqual(response.status_code, 200)
        like_count = response.json().get("likes")
        self.assertEqual(like_count, 1)

    def test_action_unlike(self):
        client = self.get_client()
        response = client.post("/api/notions/action/",
                               {"id": 2, "action": "like"})
        self.assertEqual(response.status_code, 200)
        response = client.post("/api/notions/action/",
                               {"id": 2, "action": "unlike"})
        self.assertEqual(response.status_code, 200)
        like_count = response.json().get("likes")
        self.assertEqual(like_count, 0)

    def test_action_share(self):
        client = self.get_client()
        response = client.post("/api/notions/action/",
                               {"id": 2, "action": "share"})
        self.assertEqual(response.status_code, 201)
        data = response.json()
        new_notion_id = data.get("id")
        self.assertNotEqual(new_notion_id, 2)
        self.assertEqual(self.currentCount + 1, new_notion_id)

    def test_notion_create_api_view(self):
        request_data = {"content": "this is my test notion"}
        client = self.get_client()
        response = client.post("/api/notions/create/", request_data)
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        new_notion_id = response_data.get("id")
        self.assertEqual(self.currentCount + 1, new_notion_id)

    def test_notion_detail_api_view(self):
        client = self.get_client()
        response = client.get("/api/notions/1/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        _id = data.get("id")
        self.assertEqual(_id, 1)

    def test_notion_delete_api_view(self):
        client = self.get_client()
        response = client.delete("/api/notions/1/delete/")
        self.assertEqual(response.status_code, 200)
        response = client.delete("/api/notions/1/delete/")
        self.assertEqual(response.status_code, 404)
        response_incorrect_owner = client.delete("/api/notions/3/delete/")
        self.assertEqual(response_incorrect_owner.status_code, 401)
