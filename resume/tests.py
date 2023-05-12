from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient

from resume.models import Resume, SpecialityChoices


class ResumeTestCase(TestCase):
    url = "/api/resume/"

    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="testuser", password="testpassword")
        cls.user2 = User.objects.create_user(username="testuser2", password="testpassword2")
        cls.api_client = APIClient()
        cls.resume = Resume.objects.create(owner=cls.user, status=Resume.StatusChoices.published,
                                           grade="middle", specialty=SpecialityChoices.backend,
                                           salary=100000, experience=12, education=Resume.EducationChoices.university,
                                           title="Test resume", portfolio="https://example.com",
                                           phone="1234567890", email="demo@example.com")
        super().setUpClass()

    def test_get(self):
        response = self.api_client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.api_client.force_authenticate(user=None)

    def test_patch_permissions(self):
        response = self.api_client.patch(f"{self.url}{self.resume.id}/", data={"title": "New title"})
        self.assertEqual(response.status_code, 403)
        self.api_client.force_authenticate(user=self.user2)
        response = self.api_client.patch(f"{self.url}{self.resume.id}/", data={"title": "New title"})
        self.assertEqual(response.status_code, 403)
        self.resume.refresh_from_db()
        self.assertNotEqual(self.resume.title, "New title")
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.patch(f"{self.url}{self.resume.id}/", data={"title": "New title"})
        self.assertEqual(response.status_code, 200)
        self.resume.refresh_from_db()
        self.assertEqual(self.resume.title, "New title")
        self.api_client.force_authenticate(user=None)
