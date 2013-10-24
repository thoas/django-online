from django.core.cache import cache

from . import settings
from .compat import User


class OnlineBackend(object):
    def equivalence(self, user):
        return [
            (lambda user: isinstance(user, User), lambda user: user.pk),
        ]

    def _make_key(self, key):
        return '%s%s' % (settings.ONLINE_PREFIX, key)

    def make_key(self, user):
        for test, result in self.equivalence(user):
            if test(user):
                return self._make_key(result(user))

        return self._make_key(user)

    def add(self, user):
        return cache.set(self.make_key(user), True, self.get_timeout())

    def get_timeout(self):
        return settings.ONLINE_COUNT_TIMEOUT

    def remove(self, user):
        return cache.delete(self.make_key(user))

    def exists(self, user):
        return bool(cache.get(self.make_key(user)))

    def exists_many(self, users):
        keys = dict((self.make_key(user), user) for user in users)

        results = cache.get_many(keys)

        return dict((keys[k], v) for k, v in results.iteritems())
