#!/usr/bin/python

import sys

arguments = sys.argv[1:]
count = len(arguments)

varForLoop = int(arguments[0])

for OuterForLoopCounter in range(1,varForLoop):
	PrimeNumberFlag = 0
	for InnerForLoopCounter in range(2,OuterForLoopCounter):
		if(OuterForLoopCounter%InnerForLoopCounter==0):
			PrimeNumberFlag = PrimeNumberFlag + 1

	if(PrimeNumberFlag > 0):
		print ("\tCurrent Value of For Counter\t",OuterForLoopCounter, "\tPrime Status\tNotPrime")
	else:
		print ("\tCurrent Value of For Counter\t",OuterForLoopCounter, "\tPrime Status\tPrime")