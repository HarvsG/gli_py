from gli_py.glinet import GLinet

# for dev only
if __name__ == "__main__":
    # read password from file
    with open('router_pwd', 'r') as file:
        pwd = str(file.read())

    # create an example router
    import asyncio
    router = GLinet(base_url="http://192.168.0.1/cgi-bin/api/", sync=False, token="736169463cda49c69632978616cdceb4")
    asyncio.run(router.async_connected_clients())
