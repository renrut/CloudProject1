#!/bin/python
#
# sample http client
#
import sys
import httplib
import time


def getNumber(num):
    httpCall(str(num))

def scaleServer(name):
    print "scaling"

def httpCall (path):

    # "Instantiating a connection obj"
    conn = httplib.HTTPConnection ("localhost", "8080")
    # "sending a GET request to our http server"
    start = time.time()
    conn.request ("GET", "/" + path)
    # "retrieving a response from http server"
    resp = conn.getresponse ()
    end = time.time()

    connTime = end-start
    print connTime

    # "printing response headers"
    for hdr in resp.getheaders ():
        print hdr
    # "printing data"
    data = resp.read ()
    # "Length of data = ", len(data)
    # data

