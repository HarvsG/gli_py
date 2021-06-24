from uplink.decorators import MethodAnnotation
from uplink.clients.io import RequestTemplate

class CachingTemplate(decorators.RequestTemplate):
    def __init__(self, cache, base_url, hours):
        self._cache = cache
        self._base_url = base_url
        self._hours = hours

    def before_request(self, request):
        method, url, params = request
        urlpath = url.replace(self._base_url, '')
        try:
            loaded_data =self._cache.load_cached(urlpath, self._hours)
            resp = Response()
            resp.status_code = 200
            resp._content = loaded_data
            return transitions.finish(resp)
        except Exception as e:
            pass

    def after_response(self, request, response):
        method, url, params = request
        urlpath = url.replace(self._base_url, '')
        self._cache.save_cache(urlpath, response)


class cache(MethodAnnotation):
    def __init__(self, cache_hours):
        self._cache_hours = cache_hours

    def modify_request(self, request_builder):
        cache = getattr(request_builder.client, '_cache', None)
        if cache:
            request_builder.add_request_template(CachingTemplate(cache, request_builder.base_url, self._cache_hours))