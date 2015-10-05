#from novaclient import client
import sys
import socket 

#nova = client.Client(VERSION, USERNAME, PASSWORD, PROJECT_ID, AUTH_URL)




host = 'localhost' 
port = 10080 
size = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
input_num = 0
s.connect((host,port))


while input_num != -1:
	
	input_num = input("Enter a number (-1 to disconnect): ")
	s.send(str(input_num)) 
	data = s.recv(size) 
	print 'Received:' + str(input_num) + ' is ' + data

s.close() 
