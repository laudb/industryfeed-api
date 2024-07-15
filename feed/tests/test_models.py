import uuid
from django.test import TestCase
from feed.models import User, Company, Feed, Location, Website, Category


class UserTestCase(TestCase):
    def setUp(self):
        self.first_name = "Niobe"

    def test_user_is_created(self):
        """Created user should have first_name"""
        self.user = User.objects.create(
            first_name=self.first_name,
            last_name="Moonwalker",
            username="niomoon",
            password="user-pass-1",
            phone_number="+2331111111",
            country="Angola",
        )
        self.assertEqual(self.user.first_name, self.first_name)


class CompanyTestCase(TestCase):

    def setUp(self):
        self.company_name = "Sierra Nevada Corporation"

    def test_company_is_created(self):
        """Created company should have name"""
        company = Company.objects.create(
            signature=f"{uuid.uuid4()}",
            name=self.company_name,
            details="Sierra Space Corporation, \
                is a privately held aerospace and space technologies \
                    company headquartered in Louisville, Colorado.",
        )
        self.assertEqual(company.name, self.company_name)


class LocationTestCase(TestCase):

    def setUp(self):
        self.lat = 39.96364609663782
        self.long = -105.11771531999463
        self.lat2 = 30.54705448592208
        self.long2 = -97.81581810529522
        self.country = "U.S.A."
        self.location_company_name = "Sierra Space Corp."

        self.location_company = Company.objects.create(
            signature=f"{uuid.uuid4()}",
            name=self.location_company_name,
            details="Sierra Space Corp., \
                is a privately held aerospace and space technologies \
                    company headquartered in Louisville, Colorado.",
        )

    def test_location_has_gps(self):
        """Created locations should return lat-long values"""
        location = Location.objects.create(
            lat=self.lat,
            long=self.long,
            town="Louisville",
            state="Colorado",
            country=self.country,
            company=self.location_company,
        )
        lat, long = location.gps
        self.assertEqual(lat, self.lat)
        self.assertEqual(long, self.long)


class WebsiteTestCase(TestCase):

    def setUp(self):
        self.website_company_name = "Sierra Space"
        self.website_url = "https://www.sierraspace.com/"
        self.website_company = Company.objects.create(
            signature=f"{uuid.uuid4()}",
            name=self.website_company_name,
            details="Sierra Space, \
                is a privately held aerospace and space technologies \
                    company headquartered in Louisville, Colorado.",
        )

    def test_website_is_created(self):
        """Created website should have url"""
        website = Website.objects.create(
            name=self.website_company_name,
            type=Website.WEBSITE_TYPES[0],
            url=self.website_url,
            company=self.website_company,
        )

        self.assertEqual(website.url, self.website_url)
