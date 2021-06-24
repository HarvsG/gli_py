# gli-py
A python 3 API wrapper for GL-inet routers. [WIP]

[GL-inet](https://www.gl-inet.com/) routers are built on [OpenWRT](https://openwrt.org/). They are highly customizeable but have an attractive user interface.

As part of their modiification of the UI they provide a [locally accessible API](https://dev.gl-inet.com/api/#api-SmartHome).

I thought it would be handy to develop a python 3 wrapper for the API for easy intergation into other services such as [HomeAssistant](https://www.home-assistant.io/)

Todo list:
- [ ] Decide on useful endpoints to expose
- [ ] Expose said enpoints
- [ ] Write tests
- [ ] Package correctly
- [ ] Test that dev enviroment is re-producable
- [ ] Publish on pip