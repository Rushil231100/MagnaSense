import serial
from Arduino import Arduino
import time
import datetime
import math
import numpy as np

import collections

a1 = serial.Serial('COM5',baudrate = 9600)
a2 = serial.Serial('COM6',baudrate = 9600)

q1 = collections.deque()
q2 = collections.deque()

n =10
i=0
while i<n:
	q1.append(0)
	q2.append(0)
	i+=1

avgn1 = 0
avgn2 = 0
#check 
print("average set")
x1=[]
y1=[]
z1=[]
x2=[]
y2=[]
z2=[]

j=0
while j<200:
	j+=1
	print(j)
	try:
		tdata1 = a1.readline().decode('ascii')
		tdata2 = a2.readline().decode('ascii')

		splitted = tdata1.split(',')
		#print(splitted)
		splitted[2] = splitted[2].strip('\n')
		splitted[2] = splitted[2].strip('\r')
		if (len(splitted)==3):
			x,y,z = map(int,splitted)
			x1.append(x)
			y1.append(y)
			z1.append(z)
		splitted = tdata2.split(',')
		#print(splitted)
		splitted[2] = splitted[2].strip('\n')
		splitted[2] = splitted[2].strip('\r')
		if (len(splitted)==3):
			x,y,z = map(int,splitted)
			x2.append(x)
			y2.append(y)
			z2.append(z)

	except KeyboardInterrupt:
		print("CTRL + C KEY PRESSED")
		break
	except Exception as e:
		print(e)

print(int(sum(x1)/len(x1)),int(sum(y1)/len(y1)),int(sum(z1)/len(z1)))
print(int(sum(x2)/len(x2)),int(sum(y2)/len(y2)),int(sum(z2)/len(z2)))

