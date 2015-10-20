#!/usr/bin/env python
import os
import sys
import time
from novaclient import client

# Institution: Vanderbilt University
# Code created for the CS4287-5287 course
# Author: Aniruddha Gokhale
# Created: Fall 2015

# The purpose of this code is to show how to create a server using the nova API.

####THIS CODE MODIFIED BY ALAN SAMANTA#####

# get our credentials from the environment variables
def get_nova_creds ():
    d = {}
    d['version'] = '2'  # because we will be using the version 2 of the API
    # The rest of these are obtained from our environment. Don't forget
    # to do "source cloudclass-rc.sh"
    #
    d['username'] = os.environ['OS_USERNAME']
    d['api_key'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_id'] = os.environ['OS_TENANT_NAME']
    # d['tenant_id'] = os.environ['OS_TENANT_ID']
    return d

ID=0

def startServer(server_name):
    #initialized every time, might be bad, whatever
    global ID
    creds = get_nova_creds()
    try:
        nova = client.Client (**creds)
    except:
        print "Exception thrown: ", sys.exc_info()[0]
        raise

    imageref = nova.images.find (name="alan_turner_snapshot")
    flavorref = nova.flavors.find (name="m1.small")
    sgref = nova.security_groups.find (name="default")

    attrs = {
        'name' : server_name+str(ID),
        'image' : imageref,
        'flavor' : flavorref,
        # providing the ref this way for security group is not working
        #'security_groups' : sgref,
        #'key_name' : 'gokhale_horizonisis',
        # I was going to do the following but does not work
        # 'nics' : [{'net-id' : netref.id}]
        'nics' : [{'net-id' : 'b16b0244-e1b5-4d36-90ff-83a0d87d8682'}],
        'user-data' : "/repo/CloudProject1/user_data.sh",
        'key-name' : "ISIS_cloud_ssh"
        }
    
    try:
        server = nova.servers.create (**attrs)
    except:
        print "Exception thrown: ", sys.exc_info()[0]
        raise

    # we need to check if server is up
    while (server.status != 'ACTIVE'):
        print "Not active yet; sleep for a while"
        time.sleep (2)
        # we need to retrieve the status of the server from
        # the restful API (it does not get updated dynamically in the
        # server object we have)
        server = nova.servers.find (name=(server_name+str(ID)))
    ID+=1
    return server