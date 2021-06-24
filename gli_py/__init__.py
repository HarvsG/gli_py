from glinet import GLinet

# for dev only
if __name__=="__main__":
    # read password from file
    with open('router_pwd', 'r') as file:
        pwd = str(file.read())
    
    #create an example router
    my_router = GLinet("http://192.168.0.1/cgi-bin/api/",pwd)

    # get mac (requires auth)
    print(my_router.router_mac())