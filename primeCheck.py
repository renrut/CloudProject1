
import sys
import socket 


#prime check fnct
def isPrime(myPrime):
	possibilities = int(myPrime/2)
	#edge case 1
	if(myPrime is 1):
		return "Prime"

	for i in range(2,possibilities):
		if(myPrime%i==0):
			return "Not Prime"

	return "Prime"


#Notes. Sockets must pass either buffer or, in this case, string



#host needs to change
host = 'localhost' 
#port will be 80
port = 9080
#5 client connections 
backlog = 1
size = 1024 
#binds and listens
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(backlog) 
client, address = s.accept() 

#Start values
data = "0"
prime = False

#checks for prime, sends back
while data != "-1": 
    data = client.recv(size) 
    if data and data != "-1": 
    	print data
    	prime = isPrime(int(data))
        client.send(prime) 
client.close()

