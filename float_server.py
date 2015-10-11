import sys
import socket 


#all of these ports should be port 80 (TCP) on the cloud and hosts will change
host = 'localhost' 
port = 8080 


workPort1 = 9080 
#workPort2 = 8080 

#5 clients
backlog = 5 
size = 1024 

#sets up client socket and listens and accepts when client connects
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
clientSocket.bind((host,port)) 
clientSocket.listen(backlog) 
client, address = clientSocket.accept()



#setting up a socket with the primechecker server
workSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
workSocket.connect((host,workPort1))

#init to date = "1"
data = "0"
#-1 is the exit value
while data != "-1": 
    #recieving data from client
    data = client.recv(size) 
    #check for data
    if data: 
        #print for debugging purpose
        print data
        #send data to primeChecker this is where you'll need to implement the load balancer
        workSocket.send(data)
        #recieve data from prime check server
        primeVal = workSocket.recv(size)
        #if primeval exists, send back
        if primeVal:
            client.send(primeVal)

#close sockets
client.close()
workSocket.close()
