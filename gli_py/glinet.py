from uplink import Consumer, get, post, Query, headers, returns, response_handler, Field #, Path
#import cache
from error_handling import raise_for_status


# typical base url http://192.168.8.1/cgi-bin/api/
class GLinet(Consumer):
    """A Python Client for the GL-inet API."""

    def __init__(self, password : str, **kwargs):
        #initialise the super class
        super(GLinet, self).__init__(**kwargs)

        # use the token for auth for all requests henceforth
        self.session.headers["Authorization"] = self.login(password)

    @response_handler(raise_for_status)
    @returns.json(key="token")
    @post("router/login")
    def login(self, pwd: Field):
        """fetches token"""
        # TODO deal with errors

    #@cache(hours=3)
    @returns.json(key="model")
    @get("router/model")
    def router_model(self):
        """Retrieves the router's model, no auth required"""

    @response_handler(raise_for_status)
    @returns.json(key="mac")
    @get("router/mac/get")
    def router_mac(self):
        """Retrieves the router's model"""