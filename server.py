# !/bin/python
import time
import SimpleHTTPServer
import BaseHTTPServer
import primeCheck
import sys
import httplib

HOST = "localhost"
PORT = 8080
PRIMEPORT = 9080



# MyHTTPHandler inherits from BaseHTTPServer.BaseHTTPRequestHandler
class MyHTTPHandler (SimpleHTTPServer.SimpleHTTPRequestHandler):
    
    #this should use the load balancer
    def primeHandler(s, num):
        print "Instantiating a connection obj"
        conn = httplib.HTTPConnection ("localhost", PRIMEPORT)
        print "sending a GET request to our http server"
        conn.request ("GET", "/" + num)
        resp = conn.getresponse()
        data = resp.read()
        print "data: " + data
        return data


    def scaleHandler(s):
        #TODO: Scale instance, return ip to instance
        return "scale"


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


