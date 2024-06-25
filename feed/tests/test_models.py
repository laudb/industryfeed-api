import uuid
from django.test import TestCase
from feed.models import User, Company, Feed, Location, Website, Category


user1=User.objects.create(
    first_name="Jean",
    last_name="Skywalker",
    username="jeanSky",
    password="user-pass-0",
    phone_number="+2330000000",
    country="Belgium",
)

company1 = Company.objects.create(
    signature=f"SNC-{uuid.uuid4()}",
    name="Sierra Nevada Corporation",
    details="Sierra Space Corporation, \
        is a privately held aerospace and space technologies \
            company headquartered in Louisville, Colorado.",
)

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(
            first_name="Niobe",
            last_name="Moonwalker",
            username="niomoon",
            password="user-pass-1",
            phone_number="+2331111111",
            country="Angola",
        )


class CompanyTestCase(TestCase):
    def setUp(self):

        self.lat1 = 39.96364609663782
        self.long1 = -105.11771531999463
        self.lat2 = 30.54705448592208
        self.long2 = -97.81581810529522

        self.company2 = Company.objects.create(
            signature=f"FA-{uuid.uuid4()}",
            name="Firefly Aerospace",
            details="Firefly Aerospace is an American private aerospace \
                firm based in Cedar Park, Texas, that develops launch \
                    vehicles for commercial launches to orbit. ",
        )

        self.website1 = Website.objects.create(
            name=self.company1.name,
            type=Website.WEBSITE_TYPES[0],
            url="https://www.sierraspace.com/",
            company=company1,
        )

        self.website2 = Website.objects.create(
            name=self.company2.name,
            type=Website.WEBSITE_TYPES[0],
            url="https://fireflyspace.com/",
            company=self.company2,
        )

        self.location1 = Location.objects.create(
            lat=self.lat1,
            long=self.long1,
            town="Louisville",
            state = "Colorado"
            country="U.S.A.",
            company=company1,
        )

        self.location2 = Location.objects.create(
            lat=self.lat2,
            long=self.long2,
            town="Cedar Park",
            state = "Texas"
            country="U.S.A.",
            company=self.company2,
        )

    def test_location_has_gps(self):
        """Created locations should return lat-long values"""
        lat, long = self.location1.gps()
        self.assertEqual(lat, self.lat1)
        self.assertEqual(long, self.lat2)


class FeedTestCase(TestCase):
    def setUp(self):
        feed = Feed.objects.create(
            name="feed1",
            code=uuid.uuid4(),
            owner=user1
        )
        feed.company.add(company1)


class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(
            name="Finance",
            type=Category.CATEGORY_TYPES[0]
        )


class Post(TestCase):
    def setUp(self):
        Post.objects.create(
            content="Lorem ipsum upsum",
            company=company1
        )