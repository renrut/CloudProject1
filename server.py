# !/bin/python
import time
import SimpleHTTPServer
import BaseHTTPServer
import primeCheck

HOST = "localhost"
PORT = 8080




# MyHTTPHandler inherits from BaseHTTPServer.BaseHTTPRequestHandler
class MyHTTPHandler (SimpleHTTPServer.SimpleHTTPRequestHandler):
    def parseRequest(s, req):
        reqList = req.split("/")
        
        if reqList[1] == "isPrime":
            return primeCheck.isPrime(reqList[2])
        elif reqList[1] == "scale":
            ##NEED TO SCALE HERE BY CALLING ADD INSTANCE!
            return "scale"
        else:
            return reqList
        #result = getattr(primeCheck, reqList[1])(reqList[2])
        

    def do_GET (s):
        print "get called"
        # "GET request received; reading the request"
        # the parameter s is the "self" param
        req = s.path
        print "Received request = ", req

        resp = s.parseRequest(req)

        s.send_response (200)
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


