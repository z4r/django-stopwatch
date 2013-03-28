import mock
from django.core.urlresolvers import ResolverMatch
from django.http import HttpRequest, HttpResponse
from django.test import TestCase
from stopwatch.middleware import StopWatchMiddleware


def func():
    pass


class StopWatchMiddlewareTestCase(TestCase):
    def setUp(self):
        self.mw = StopWatchMiddleware()
        self.request = HttpRequest()
        self.request.method = 'GET'
        self.request.resolver_match = ResolverMatch(func, (), {}, url_name='resource_list' ,namespaces=['namespace'])
        self.response = HttpResponse()
        self._statsd_patch = mock.patch('statsd.Client')
        self.mock_client = self._statsd_patch.start()

    def tearDown(self):
        self._statsd_patch.stop()

    def test_process_request(self):
        with mock.patch('time.time') as time_time:
            time_time.return_value = 1
            self.mw.process_request(self.request)
        self.assertEqual(getattr(self.request, '_stopwatch_start'), 1)

    def test_process_response(self):
        self.request._stopwatch_start = 1
        with mock.patch('time.time') as time_time:
            time_time.return_value = 2
            self.mw.process_response(self.request, self.response)
        self.mock_client._send.assert_called_with(mock.ANY, {
            'stopwatch.namespace.resource_list.GET.200': '1000|ms'
        })
