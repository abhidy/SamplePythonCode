#!/usr/bin/python

import sys
import time;



arguments = sys.argv[1:]
count = len(arguments)

varForLoop = int(arguments[0])

localtime1 = time.asctime( time.localtime(time.time()) )
for OuterForLoopCounter in range(1,varForLoop):
	PrimeNumberFlag = 0
	for InnerForLoopCounter in range(2,OuterForLoopCounter):
		if(OuterForLoopCounter%InnerForLoopCounter==0):
			PrimeNumberFlag = PrimeNumberFlag + 1
			break

	#if(PrimeNumberFlag > 0):
		#print ("\tCurrent Value of For Counter\t",OuterForLoopCounter, "\tPrime Status\tNotPrime")
	if(PrimeNumberFlag == 0):
		print ("\tCurrent Value of For Counter\t",OuterForLoopCounter, "\tPrime Status\tPrime")
		
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time Start:", localtime1)
print ("Local current time End:", localtime)	