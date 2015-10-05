
import sys
import socket 


def isPrime(myPrime):
	possibilities = int(myPrime/2)
	if(myPrime is 1):
		return "Prime"

	for i in range(2,possibilities):
		if(myPrime%i==0):
			return "Not Prime"

	return "Prime"


host = 'localhost' 
port = 9080 
backlog = 5 
size = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(backlog) 
client, address = s.accept() 
data = "1"
prime = False

while data != "-1": 
    data = client.recv(size) 
    if data and data != "-1": 
    	print data
    	prime = isPrime(int(data))
        client.send(prime) 
client.close()

