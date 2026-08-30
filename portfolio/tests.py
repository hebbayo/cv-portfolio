from django.test import TestCase
from django.urls import reverse

from .models import Profile, Project, ContactMessage


class ApiTests(TestCase):
    def setUp(self):
        Profile.objects.create(full_name="Ali", title="Dev", bio="hi", email="a@b.com")
        Project.objects.create(
            title="P", slug="p", summary="s", description="d", tech_stack="Django, JS",
        )

    def test_resume(self):
        data = self.client.get(reverse("resume")).json()
        self.assertEqual(data["profile"]["full_name"], "Ali")
        self.assertEqual(data["projects"][0]["tech_stack"], ["Django", "JS"])

    def test_project_detail_404(self):
        self.assertEqual(self.client.get("/api/projects/nope/").status_code, 404)

    def test_contact(self):
        r = self.client.post(
            reverse("contact"),
            {"name": "X", "email": "x@y.com", "message": "hello"},
            content_type="application/json",
        )
        self.assertEqual(r.status_code, 201)
        self.assertEqual(ContactMessage.objects.count(), 1)

    def test_contact_rejects_bad_email(self):
        r = self.client.post(
            reverse("contact"),
            {"name": "X", "email": "nope", "message": "hello"},
            content_type="application/json",
        )
        self.assertEqual(r.status_code, 400)
        self.assertEqual(ContactMessage.objects.count(), 0)

    def test_cors_header_for_allowed_origin(self):
        with self.settings(CORS_ALLOWED_ORIGINS=["http://localhost:5173"]):
            r = self.client.get(reverse("resume"), HTTP_ORIGIN="http://localhost:5173")
            self.assertEqual(
                r["Access-Control-Allow-Origin"], "http://localhost:5173"
            )
