from django.test import TestCase
from django.core.urlresolvers import reverse


class SimpleTests(TestCase):
    def test_online(self):
        response = self.client.get(reverse('online_test'))

        self.assertEqual(response.status_code, 200)
