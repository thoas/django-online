from django.conf.urls import patterns, url

from online.tests.views import test


urlpatterns = patterns(
    '',
    url(r'^test/$',
        test,
        name='online_test'),
)
