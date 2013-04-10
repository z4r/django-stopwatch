import time
from stopwatch import loader, errors


class StopWatchMiddleware(object):
    def __init__(self):
        self.keybuilder = loader.get_keybuilder()
        self.backends = loader.get_backends()

    def process_request(self, request):
        request._stopwatch_start = time.time()

    def process_response(self, request, response):
        if getattr(request, '_stopwatch_start', None):
            delta = time.time() - request._stopwatch_start
            try:
                key = self.keybuilder.build(request, response)
                for backend in self.backends:
                    backend.push(key=key, delta=delta)
            except errors.KeyBuilderException:
                pass
        return response
