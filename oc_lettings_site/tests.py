from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser
from oc_lettings_site.views import index


def test_dummy():
    assert 1


class Index(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index(self):
        request = self.factory.get("/")
        request.user = AnonymousUser()
        response = index(request)
        self.assertEqual(response.status_code, 200)
