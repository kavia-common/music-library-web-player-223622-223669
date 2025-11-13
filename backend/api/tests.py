from django.test import TestCase, Client
from django.urls import reverse

class HealthTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_health(self):
        url = reverse('Health')  # Make sure the URL is named
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"message": "Server is up!"})
