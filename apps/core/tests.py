from django.test import TestCase, SimpleTestCase
from django.urls import reverse


class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("core:about"))
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(reverse("core:about"))
        self.assertTemplateUsed(response, "core/about.html")

    def test_template_content(self):
        response = self.client.get(reverse("core:about"))
        self.assertContains(response, "<title>About Us</title>")


class PrivacypageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/policy/")
        self.assertEqual(response.status_code, 200)

    def test_policy_page(self):
        response = self.client.get(reverse("core:policy"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/policy.html")
        self.assertContains(response, "Privacy Policy")
