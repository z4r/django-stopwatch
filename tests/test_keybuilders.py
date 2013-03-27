from django.core.urlresolvers import ResolverMatch
from django.http import HttpRequest, HttpResponse
from django.test import TestCase
from stopwatch.keybuilders import RestApiKeyBuilder


def func():
    pass


class RestApiKeyBuilderTestCase(TestCase):
    def setUp(self):
        self.keybuilder = RestApiKeyBuilder()
        self.request = HttpRequest()
        self.request.method = 'GET'
        self.request.resolver_match = ResolverMatch(func, (), {}, namespaces=['namespace'])
        self.response = HttpResponse()

    def test_build(self):
        key = self.keybuilder.build(self.request, self.response)
        self.assertEqual(key, 'namespace.tests.test_keybuilders.func.GET.200')
