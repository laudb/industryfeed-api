import uuid, unittest
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory, TestCase, Client
from feed.models import User, Website

from feed.views import WebsiteViewSet


class WebsiteTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_websites_endpoint_for_forbidden_response(self):
        """
        Get forbidden response for unauthenticated request
        """
        response = self.client.get("/api/v1/websites/")
        self.assertEqual(response.status_code, 403)


class CompanyTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_website_for_success_response(self):
        """
        Get success response for unauthenticated request
        """
        response = self.client.get("/api/v1/companies/")
        self.assertEqual(response.status_code, 200)

    def test_website_for_not_found_response(self):
        """
        Get not found response for unauthenticated request
        """
        response = self.client.get("/api/v1/companies/1/")
        self.assertEqual(response.status_code, 404)
