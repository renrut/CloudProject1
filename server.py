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
    lb=RRLoadBalancer(["10.10.3.119"])

    #this should use the load balancer
    def primeHandler(self, num):
        resp=self.lb.newJob(num)
        data = resp.read()
        print "data: " + data
        return data


    def scaleHandler(s):
        #TODO: Scale instance, return ip to instance
        new_server=create_server.startServer("AS_TS_SERVER")
        self.lb.addServer(new_server.networks["b16b0244-e1b5-4d36-90ff-83a0d87d8682"])

    def parseRequest(s, req):
        reqList = req.split("/")
        
        if reqList[1] == "isPrime":
            return s.primeHandler(reqList[2])

        elif reqList[1] == "scale":
            #NEED TO SCALE HERE BY CALLING ADD INSTANCE!
            #Need to store internal address
            return scaleHandler()

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


