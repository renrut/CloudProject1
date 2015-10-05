import sys
import socket 


#all of these ports should be port 80 (TCP) on the cloud
host = 'localhost' 
port = 10080 


workPort1 = 9080 
#workPort2 = 10080 

backlog = 5 
size = 1024 

#sets up client socket and listens and accepts
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
clientSocket.bind((host,port)) 
clientSocket.listen(backlog) 
client, address = clientSocket.accept()



#setting up a socket with the primechecker
workSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
workSocket.connect((host,workPort1))

data = "1"
#-1 is the exit value
while data != "-1": 
    #recieving data from client
    data = client.recv(size) 
    if data: 
        #print for debugging purpose
        print data
        #send data to primeChecker this is where you'll need to implement the load balancer
        workSocket.send(data)
        primeVal = workSocket.recv(size)
        
        if primeVal:
            client.send(primeVal)

client.close()



# host = 'localhost' 
# size = 1024 
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# input_num = 0
# s.connect((host,port))


# while input_num != -1:
    
#   input_num = input("Enter a number (-1 to disconnect): ")
#   s.send(str(input_num)) 
#   data = s.recv(size) 
#   print 'Received:' + input_num 'is' + data

# s.close() 
