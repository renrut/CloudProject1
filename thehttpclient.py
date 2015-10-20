#!/bin/python
#
# sample http client
#
import sys
import httplib
import time


def getNumber(num):
    httpCall("isPrime"  + "/" + str(num) )


def scaleServer(name):
    httpCall("scale")

def httpCall (path):
    SERVERNAME = "server2"
    SCALETIME = 1

    print "Instantiating a connection obj"
    conn = httplib.HTTPConnection ("localhost", "8080")
    print "sending a GET request to our http server"
    start = time.time()
    conn.request ("GET", "/" + path)
    # "retrieving a response from http server"
    resp = conn.getresponse ()
    end = time.time()
    print ""
    connTime = end-start
    print connTime
    #Arbitrary scale value.
    if connTime > SCALETIME:
        scaleServer(SERVERNAME)
    # "printing response headers"
    for hdr in resp.getheaders ():
        print hdr
    # "printing data"
    data = resp.read()
    print data
    # "Length of data = ", len(data)
    # data

