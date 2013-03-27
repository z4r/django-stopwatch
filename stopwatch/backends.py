from django.conf import settings
from statsd import Connection, Timer


class StatsDStopWatchBackend(object):
    def __init__(self):
        self.client = Timer(
            name=getattr(settings, 'STOPWATCH_STATSD_PREFIX', 'stopwatch'),
            connection=Connection(
                host=getattr(settings, 'STOPWATCH_STATSD_HOST', None),
                port=getattr(settings, 'STOPWATCH_STATSD_PORT', None),
            ),
        )

    def push(self, key, delta):
        self.client.send(subname=key, delta=delta)
