from requests.models import Response
from json import loads
import asyncio
import uplink
class UnsuccessfulRequest(Exception):
    '''raised when the status code is not 200'''


class NonZeroResponse(Exception):
    '''raised when the router responds but with a non O code'''


def raise_for_status(response: Response):
    if type(response) is not uplink.clients.aiohttp_.ThreadedResponse:
        def proc_res(response):
            """Checks whether or not the response was successful."""
            print(type(response))
            print("sync response")
            if 200 <= response.status_code < 300:
                # Pass through the response.
                res = loads(response.text)
                # Gl-inet's api uses its own error codes that are returned in
                # status 200 messages - this is out of spec so we must handle it
                if res['code'] < 0:
                    if 'msg' not in res:
                        res['msg'] = "null"

                    raise NonZeroResponse("Request returned error code %s with message:' %s'" % (res['code'], res['msg']))
                return res
    else:
        async def proc_res(response):
            """Checks whether or not the response was successful."""
            if 200 <= response.status < 300:
                # Pass through the response.
                res = loads(response.text())
                # Gl-inet's api uses its own error codes that are returned in
                # status 200 messages - this is out of spec so we must handle it
                if res['code'] < 0:
                    if 'msg' not in res:
                        res['msg'] = "null"

                    raise NonZeroResponse("Request returned error code %s with message:' %s'" % (res['code'], res['msg']))
                return res
    return proc_res(response)

    raise UnsuccessfulRequest(response.url)
