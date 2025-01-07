from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from profiles.models import Profile
from profiles.views import index, profile


class ProfilesTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(username="HeadlinesGazer")
        self.profile = Profile.objects.create(user=self.user, favorite_city="Napoli")

    def test_index(self):
        request = self.factory.get("/profiles/")
        request.user = AnonymousUser()
        response = index(request)
        self.assertEqual(response.status_code, 200)

    def test_profile(self):
        request = self.factory.get("/profile/HeadlinesGazer/")
        request.user = AnonymousUser()
        response = profile(request, "HeadlinesGazer")
        self.assertEqual(response.status_code, 200)
