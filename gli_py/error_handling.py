from requests.models import Response
from json import loads

class UnsuccessfulRequest(Exception):
    '''raised when the status code is not 200'''
class NonZeroResponse(Exception):
    '''raised when the router responds but with a non O code'''

def raise_for_status(response: Response):
    """Checks whether or not the response was successful."""
    if 200 <= response.status_code < 300:
        # Pass through the response.
        res = loads(response.text)
        if res['code'] < 0:
            raise NonZeroResponse("Request returned error code %s with message:' %s'" % (res['code'], res['msg']))
        return response

    raise UnsuccessfulRequest(response.url)

