from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser
from lettings.views import index, letting
from lettings.models import Letting, Address


class LettingsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.address = Address.objects.create(
            number=1,
            street="rue de la rue",
            city="ville",
            state="region",
            zip_code=12345,
            country_iso_code="+33",
        )
        self.lettings = Letting.objects.create(title="Titre", address=self.address)

    def test_index(self):
        request = self.factory.get("/lettings/")
        request.user = AnonymousUser()
        response = index(request)
        self.assertEqual(response.status_code, 200)

    def test_lettings(self):
        request = self.factory.get("/lettings/1/")
        request.user = AnonymousUser()
        response = letting(request, 1)
        self.assertEqual(response.status_code, 200)
