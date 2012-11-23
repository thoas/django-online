from django.conf import settings

ONLINE_COUNT_TIMEOUT = getattr(settings, 'ONLINE_COUNT_TIMEOUT', 3600)

ONLINE_PREFIX = getattr(settings, 'ONLINE_PREFIX', 'mad_online_')

ONLINE_BACKEND = getattr(settings, 'ONLINE_BACKEND', 'online.backend.OnlineBackend')
