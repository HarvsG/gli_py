import functools
from typing import Union
from uplink import (
    Consumer,
    get,
    post,
    returns,
    response_handler,
    Field,
    AiohttpClient,
    timeout)
import asyncio

# , Path, clients, RequestsClient, Query, headers,response,handler,
# import cache

from error_handling import raise_for_status
# from json import loads




# typical base url http://192.168.8.1/cgi-bin/api/
@timeout(2)
@response_handler(raise_for_status)
class GLinet(Consumer):
    """A Python Client for the GL-inet API."""
    def __init__(
        self,
        token: str = None,
        sync: bool = True,
        **kwargs
    ):
        self.sync = sync
        self.client = None
        self._logged_in: bool = False
        self.token = token
        if not self.sync:
            self.client = AiohttpClient()

        # initialise the super class
        super(GLinet, self).__init__(client=self.client, **kwargs)

        if self.token is not None:
            self.logged_in = True
            self.session.headers["Authorization"] = self.token

    @post("router/login")
    def _login(self, pwd: Field):
        """fetches token"""

    async def async_login(self, password: str) -> None:
        assert(self.client is not None)
        try:
            # use the token for auth for all requests henceforth
            res = await self._login(password)
            self.token = res['token']
            self.session.headers["Authorization"] = self.token
            self._logged_in = True
        except Exception as err:
            self._logged_in = False
            raise ConnectionRefusedError("Failed to authenticate with GL-inet. Error %s", err)

    def login(self, password: str) -> None:
        assert(self.client is None)
        try:
            # use the token for auth for all requests henceforth
            res = self._login(password)
            self.token = res['token']
            self.session.headers["Authorization"] = self.token
            self._logged_in = True
            print(self.session.headers["Authorization"])
        except Exception as err:
            print("login failure")
            self._logged_in = False
            raise ConnectionRefusedError("Failed to authenticate with GL-inet. Error %s", err)

    @get("router/model")
    def router_model(self):
        """Retrieves the router's model, no auth required"""

    # Basic device interaction
    @get("router/model")
    def router_model1(self):
        """Retrieves the router's model, no auth required"""

    @get("router/mac/get")
    def router_mac(self):
        """Retrieves the router's mac address"""

    @get("router/status")
    def router_status(self):
        """router status"""

    @get("firmware/onlinecheck")
    def new_firmware(self):
        """whether there is new firmware to upgrade"""

    @get("router/reboot")
    def reboot(self):
        """reboot router"""

    # Basic WAN interaction

    @get("wan/info")
    def wan_ip(self):
        """Retrieves the router's wan ip"""

    @get("internet/public_ip/get")
    def public_ip(self):
        """Retrieves the router's public ip. Will give VPN IP is connected"""

    @get("internet/reachable")
    def connected_to_internet(self):
        """Is the internet reachable"""

    # Client information

    @get("client/list")
    def list_all_clients(self):
        """gets all clients"""

    @get("router/static_leases/list")
    def list_static_clients(self):
        """gets all static clients"""

    def connected_clients(self):
        clients = []
        all_clients = self.list_all_clients()
        for client in all_clients:
            if client['online'] is True:
                clients.append(client)
        return clients

    # VPN information

    @get("wireguard/client/status")
    def wireguard_client_state(self):
        """Retrieves the wireguard status"""

    # SMS stuff

    # TODO untested
    @get("modem/info")
    def _get_modems(self):
        """Returns a list of modems"""

    # TODO untested
    def count_modems(self) -> int:
        return len(self._get_modems())

    # TODO untested
    @get("modem/sms/status")
    def sms_status(self, modem_id: Field):
        """Retrieves the status of the SMS modem"""

    # TODO untested
    @post("modem/sms/send")
    def _send_sms(self, modem_id: Field, message: Field, number: Field):
        """send an SMS"""

    # TODO untested
    def send_sms(self, number: str, message: str):
        modems = self._get_modems()
        # if there are no modems raise exception
        if len(modems) == 0:
            raise Exception("No modems found")
        # if there is only one modem try and send the message
        elif len(modems) == 1:
            return self._send_sms(modems[0]["modem_id"], message, number)
        elif len(modems) > 1:
            for modem in modems:
                if modem["SIM_status"] == 0:
                    return self._send_sms(modem["modem_id"], message, number)

    @property
    def logged_in(self):
        return self._logged_in
