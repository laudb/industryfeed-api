import unittest, uuid
from django.contrib.auth.models import AnonymousUser
from feed.models import Company
from django.test import Client


class WebsiteTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_websites_endpoint_for_forbidden_response(self):
        """
        Get forbidden response for unauthenticated request on websites/
        """
        response = self.client.get("/api/v1/websites/")
        self.assertEqual(response.status_code, 401)


class FeedTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_feeds_endpoint_for_forbidden_response(self):
        """
        Get forbidden response for unauthenticated request on feeds/
        """
        response = self.client.get("/api/v1/feeds/")
        self.assertEqual(response.status_code, 401)


class LocationTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_websites_endpoint_for_forbidden_response(self):
        """
        Get forbidden response for unauthenticated request on locations/
        """
        response = self.client.get("/api/v1/locations/")
        self.assertEqual(response.status_code, 401)


class CompanyTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.company_name = "Random Company"

    def test_companies_endpoint_for_success_response(self):
        """
        Get success response for unauthenticated request
        """
        response = self.client.get("/api/v1/companies/")
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.data), 0)

    def test_companies_endpoint_for_not_found_response(self):
        """
        Get not found response for unauthenticated request
        """
        response = self.client.get("/api/v1/companies/200/")
        self.assertEqual(response.status_code, 404)

    def test_companies_endpoint_for_created_success(self):
        """
        Create a company
        """

        company = Company.objects.create(
            signature=uuid.uuid4(),
            logo="",
            name=self.company_name,
            details="Random Company since 1987",
            is_active=False,
        )
        self.assertEqual(company.name, self.company_name)

    def test_companies_endpoint_for_found_response(self):
        """
        Get not found response for unauthenticated request
        """
        response = self.client.get("/api/v1/companies/1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], self.company_name)
