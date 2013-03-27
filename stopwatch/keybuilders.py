class RestApiKeyBuilder(object):
    def build(self, request, response):
        return '.'.join(map(unicode, filter(None, [
            request.resolver_match.namespace,
            request.resolver_match.url_name,
            request.method,
            response.status_code,
        ])))
