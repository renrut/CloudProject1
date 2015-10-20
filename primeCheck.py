
import sys
import socket 
import time
import SimpleHTTPServer
import BaseHTTPServer
import primeCheck

HOST = "localhost"
PORT = 9080

# MyHTTPHandler inherits from BaseHTTPServer.BaseHTTPRequestHandler
class MyHTTPHandler (SimpleHTTPServer.SimpleHTTPRequestHandler):

    #prime check fnct
    def isPrime(s, myPrime):
        myPrime = int(myPrime)
        possibilities = int(myPrime/2)
        #edge case 1
        if(myPrime == 1):
            return "Prime"

        for i in range(2,possibilities):
            if(i%1000 == 0):
                print "."
            if(myPrime%i==0):
                return "Not Prime"
        return "Prime"

    def do_GET (s):
        print "get called"
        # "GET request received; reading the request"
        # the parameter s is the "self" param
        req = s.path
        print "Received request = ", req

        path = req.split("/")
        print path[1]
        resp = s.isPrime(path[1])
        print "resp = " + resp
        s.send_response (200)
        s.send_header ("Content-type", "text/plain")
        s.end_headers ()
        s.wfile.write (resp)


if __name__ == '__main__':
    print "Instantiating a BaseHTTPServer"
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class (("10.10.3.124", 80), MyHTTPHandler)
    try:
        print "Run a BaseHTTPServer"
        httpd.serve_forever ()
    except KeyboardInterrupt:
        pass

    httpd.server_close ()

