#Alan Samanta & Turner Strayhorn

#load balancer, keeps track of all worker servers, assigns work to them in a round robin fashion

import sys
import httplib

class RRLoadBalancer:

    #takes in a list of servers to do scheduling on
    def __init__(self, servers):
        self._port=80

        #if servers isn't a list, make it a list
        self._server_list = servers if type(servers) is list else [servers]
        #index of the next server to be assigned a job
        self._next_server = 0

    #takes in a job, passes it to the next server in the list. Job should be of the appropriate type
    def newJob(self, job):
        if not self._server_list:
            #no servers in list
            print "No servers available" 
            return None 
        resp=self._assignJob(job, self._server_list[self._next_server])
        self._incNextServer()
        return resp

    #increment next server and mod it by the length of the list
    def _incNextServer(self):
        self._next_server+=1
        self._next_server%=len(self._server_list)

    #assigns the given job to the give server
    #separate method for increased flexibility
    #server is the IP of the server
    #job is what will be passed in to get request
    def _assignJob(self, job, server):
        print "Instantiating a connection obj"
        conn = httplib.HTTPConnection (server, self._port)
        print "sending a GET request to our http server"
        conn.request ("GET", "/" + job)
        return conn.getresponse()
        

    #adds a new server to the load balancer
    def addServer(self, server):
        self._server_list.append(server)