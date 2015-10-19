
import sys
import socket 


#prime check fnct
def isPrime(myPrime):
	myPrime = int(myPrime)
	possibilities = int(myPrime/2)
	#edge case 1
	if(myPrime == 1):
		return "Prime"

	for i in range(2,possibilities):
		if(myPrime%i==0):
			return "Not Prime"

	return "Prime"

