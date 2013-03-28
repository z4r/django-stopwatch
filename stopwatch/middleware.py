import time
from stopwatch import loader


class StopWatchMiddleware(object):
    def __init__(self):
        self.keybuilder = loader.get_keybuilder()
        self.backends = loader.get_backends()

    def process_request(self, request):
        request._stopwatch_start = time.time()

    def process_response(self, request, response):
        delta = time.time() - request._stopwatch_start
        for backend in self.backends:
            backend.push(
                key=self.keybuilder.build(request, response),
                delta=delta,
            )
        return response
