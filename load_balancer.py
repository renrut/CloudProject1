#Alan Samanta & Turner Strayhorn

#load balancer, keeps track of all worker servers, assigns work to them in a round robin fashion

class RRLoadBalancer:
    
    #takes in a list of servers to do scheduling on
    def __init__(self, servers):
        #if servers isn't a list, make it a list
        self._server_list = servers if type(servers) is list else [servers]
        #index of the next server to be assigned a job
        self._next_server = 0

    #takes in a job, passes it to the next server in the list. Job should be of the appropriate type
    def newJob(self, job):
        self._assignJob(job, self._server_list[self._next_server])
        self._incNextServer()

    #increment next server and mod it by the length of the list
    def _incNextServer(self):
        self._next_server+=1
        self._incNextServer%=len(self._server_list)

    #assigns the given job to the give server
    #separate method for increased flexibility
    def _assignJob(self, job, server):
        pass

    #adds a new server to the load balancer
    def addServer(self, server):
        self._server_list.append(server)