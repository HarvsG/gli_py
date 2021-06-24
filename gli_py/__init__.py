from uplink import Consumer, get, post, Path, Query, Field, headers, returns
#import cache
from gli_py.error_handling import raise_for_status


# typical base url http://192.168.8.1/cgi-bin/api/
class GLinet(Consumer):
    """A Python Client for the GL-inet API."""

    def __init__(self, base_url : str, password : str):
        #initialise the super class
        super(GLinet, self).__init__(base_url=base_url)

        # use the token for auth for all requests henceforth
        self.session.headers["Authorization"] = self.login(password)

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

# for dev only
if __name__=="__main__":
    # read password from file
    with open('router_pwd', 'r') as file:
        pwd = str(file.read())
    
    #create an example router
    my_router = GLinet("http://192.168.0.1/cgi-bin/api/",pwd)

    # get mac (requires auth)
    print(my_router.router_mac())