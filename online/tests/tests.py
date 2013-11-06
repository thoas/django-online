from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from online.middleware import online


class SimpleTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('thoas', 'thoas@localhost', '$ecret')

    def test_online(self):
        response = self.client.get(reverse('online_test'))

        self.assertEqual(response.status_code, 200)

        self.client.login(username='thoas', password='$ecret')

        response = self.client.get(reverse('online_test'))

        self.assertEqual(response.status_code, 200)

        self.assertTrue(online.exists(self.user))
