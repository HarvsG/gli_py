from uplink import Consumer, get, post, Query, headers, returns, response_handler, Field #, Path
#import cache

from gli_py.error_handling import raise_for_status
from json import loads


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

    # Basic device interaction
    @response_handler(raise_for_status)
    @returns.json(key="model")
    @get("router/model")
    def router_model(self):
        """Retrieves the router's model, no auth required"""

    @response_handler(raise_for_status)
    @returns.json(key="mac")
    @get("router/mac/get")
    def router_mac(self):
        """Retrieves the router's mac address"""

    @response_handler(raise_for_status)
    @returns.json
    @get("router/status")
    def router_status(self):
        """router status"""

    @response_handler(raise_for_status)
    @returns.json(key="has_new")
    @get("firmware/onlinecheck")
    def new_firmware(self):
        """whether there is new firmware to upgrade"""

    @response_handler(raise_for_status)
    @returns.json
    @get("router/reboot")
    def reboot(self):
        """reboot router"""


    # Basic WAN interaction

    @response_handler(raise_for_status)
    @returns.json(key="ip")
    @get("wan/info")
    def wan_ip(self):
        """Retrieves the router's wan ip"""

    @response_handler(raise_for_status)
    @returns.json(key="serverip")
    @get("internet/public_ip/get")
    def public_ip(self):
        """Retrieves the router's public ip"""

    @response_handler(raise_for_status)
    @returns.json(key="reachable")
    @get("internet/reachable")
    def connected_to_internet(self):
        """Is the internet reachable"""

    # Client information

    @response_handler(raise_for_status)
    @returns.json(key="clients")
    @get("client/list")
    def list_all_clients(self):
        """gets all clients"""

    @response_handler(raise_for_status)
    @returns.json(key="list")
    @get("router/static_leases/list")
    def list_static_clients(self):
        """gets all static clients"""

    def connected_clients(self):
        clients = []
        all_clients = self.list_all_clients()
        for client in all_clients:
            if client['online'] ==True:
                clients.append(client)
        return clients


    # VPN information
    @response_handler(raise_for_status)
    @returns.json
    @get("wireguard/client/status")
    def wireguard_client_state(self):
        """Retrieves the wireguard status"""

    # SMS stuff

    # TODO untested
    @response_handler(raise_for_status)
    @returns.json(key="modems")
    @get("modem/info")
    def _get_modems(self):
        """Returns a list of modems"""

    # TODO untested
    def count_modems(self) -> int:
        return len(_get_modems())

    # TODO untested
    @response_handler(raise_for_status)
    @returns.json
    @get("modem/sms/status")
    def sms_status(self):
        """Retrieves the status of the SMS modem"""

    # TODO untested
    @response_handler(raise_for_status)
    @returns.json
    @post("modem/sms/send")
    def _send_sms(self, modem_id: Field, message: Field, number: Field):
        """send an SMS"""
    
    # TODO untested
    def send_sms(number: str, message: str):
        modems = _get_modems()
        # if there are no modems raise exception
        if len(modems) == 0:
            raise Exception("No modems found")
        # if there is only one modem try and send the message
        elif len(modems) == 1:
            return _send_sms(modems[0]["modem_id"], message, number)
        elif len(modems) > 1:
            for modem in modems:
                if modem["SIM_status"] == 0:
                    return _send_sms(modem["modem_id"], message, number)
        
