import mock
from django.test import TestCase
from stopwatch.backends import StatsDStopWatchBackend


class StatsDStopWatchBackendTestCase(TestCase):
    def test_send(self):
        with mock.patch('statsd.Client') as mock_client:
            backend = StatsDStopWatchBackend()
            backend.push('key', 0.01)
        mock_client._send.assert_called_once_with(mock.ANY, {'stopwatch.key': '10|ms'})
