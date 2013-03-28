from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase
from django.test.utils import override_settings
from stopwatch.backends import StatsDStopWatchBackend
from stopwatch.keybuilders import RestApiKeyBuilder
from stopwatch.loader import get_keybuilder, get_backends


class ImporterTestCase(TestCase):
    def test_get_keybuilder_default(self):
        kb = get_keybuilder()
        self.assertTrue(isinstance(kb, RestApiKeyBuilder))

    @override_settings(STOPWATCH_KEYBUILDER='stopwatch.keybuilders.RestApiKeyBuilder')
    def test_get_keybuilder(self):
        kb = get_keybuilder()
        self.assertTrue(isinstance(kb, RestApiKeyBuilder))

    @override_settings(STOPWATCH_KEYBUILDER='stopwatch')
    def test_get_keybuilder_nodot(self):
        self.assertRaises(ImproperlyConfigured, get_keybuilder)

    @override_settings(STOPWATCH_KEYBUILDER='badimport.keybuilders.RestApiKeyBuilder')
    def test_get_keybuilder_badimport(self):
        self.assertRaises(ImproperlyConfigured, get_keybuilder)

    @override_settings(STOPWATCH_KEYBUILDER='stopwatch.keybuilders.BadKeyBuilder')
    def test_get_keybuilder_badcls(self):
        self.assertRaises(ImproperlyConfigured, get_keybuilder)

    def test_get_backends_default(self):
        b = get_backends()
        self.assertTrue(isinstance(b[0], StatsDStopWatchBackend))

    @override_settings(STOPWATCH_BACKENDS=('stopwatch.backends.StatsDStopWatchBackend', ))
    def test_get_backends(self):
        b = get_backends()
        self.assertTrue(isinstance(b[0], StatsDStopWatchBackend))

    @override_settings(STOPWATCH_BACKENDS=('stopwatch',))
    def test_get_backends_nodot(self):
        self.assertRaises(ImproperlyConfigured, get_backends)

    @override_settings(STOPWATCH_BACKENDS=('badimport.backends.StatsDStopWatchBackend',))
    def test_get_backends_badimport(self):
        self.assertRaises(ImproperlyConfigured, get_backends)

    @override_settings(STOPWATCH_BACKENDS=('stopwatch.backends.BadBackend',))
    def test_get_backends_badcls(self):
        self.assertRaises(ImproperlyConfigured, get_backends)
