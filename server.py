# !/bin/python
import time
import SimpleHTTPServer
import BaseHTTPServer
import primeCheck
import sys
import httplib
from load_balancer import RRLoadBalancer
import create_server

HOST = "localhost"
PORT = 8080
PRIMEPORT = 9080



# MyHTTPHandler inherits from BaseHTTPServer.BaseHTTPRequestHandler
class MyHTTPHandler (SimpleHTTPServer.SimpleHTTPRequestHandler):
    lb=RRLoadBalancer(["10.10.3.124", "10.10.11.14"])

    #this should use the load balancer
    def primeHandler(self, num):
        resp=self.lb.newJob(num)
        data = resp.read()
        print "data: " + data
        return data


    def scaleHandler(s):
        #TODO: Scale instance, return ip to instance
        NETWORK_ID="internal network"

        new_server=create_server.startServer("AS_TS_SERVER")
        #s.lb.addServer(new_server.addresses[NETWORK_ID][0]['addr'])

    def parseRequest(s, req):
        reqList = req.split("/")
        
        if reqList[1] == "isPrime":
            return s.primeHandler(reqList[2])

        elif reqList[1] == "scale":
            #NEED TO SCALE HERE BY CALLING ADD INSTANCE!
            #Need to store internal address
            return s.scaleHandler()

        else:
            #for debugging. Probs should keep in
            return reqList
        

    def do_GET (s):

        print "get called"
        # "GET request received; reading the request"
        # the parameter s is the "self" param
        req = s.path
        print "Received request = ", req

        resp = s.parseRequest(req)
        print "resp = " + resp
        s.send_response (200)
        s.send_header ("Content-type", "text/plain")
        s.end_headers ()
        s.wfile.write (resp)


if __name__ == '__main__':
    print "Instantiating a BaseHTTPServer"
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class ((HOST, PORT), MyHTTPHandler)
    try:
        print "Run a BaseHTTPServer"
        httpd.serve_forever ()
    except KeyboardInterrupt:
        pass

    httpd.server_close ()


