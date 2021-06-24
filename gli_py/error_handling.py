def UnsuccessfulRequest(url:str):
    print("Unsuccessful request: "+ url)

def raise_for_status(response):
    """Checks whether or not the response was successful."""
    if 200 <= response.status_code < 300:
        # Pass through the response.
        print(response)
        return response

    raise UnsuccessfulRequest(response.url)