import serial
from Arduino import Arduino
import time
import datetime
import math
import numpy as np
import collections
 



earthF1 = np.array([1120,-3120,-4190 ])
modearth1 = round(np.linalg.norm(earthF1),4)
# Initializing a queue

q1 = collections.deque()
n =10
i=0
while i<10:
	q1.append(modearth1)
	i+=1
avgn1 = modearth1
print("average set")

a1 = serial.Serial('COM6',baudrate = 9600)
while True :
	try:
		tdata1 = a1.readline().decode('ascii')
		splitted = tdata1.split(',')
			#print(splitted)
		splitted[2] = splitted[2].strip('\n')
		splitted[2] = splitted[2].strip('\r')
		#print(splitted)
		if (len(splitted)==3):
			vec = np.array(list(map(int,splitted)))
			#print(vec-earthF1)
			intensity = round(np.linalg.norm(vec-earthF1),4)
			avgn1 = (avgn1*10 - q1.popleft() + intensity)/10
			q1.append(intensity)
			print(intensity,avgn1)
			#d = (param1[0]/(intensity-param1[1]))-param1[2]
			#sqrt(param1[0]/(ans-param[1]))-param1[2]
			#print(vec,vec-earthF1,int(intensity),"sqDistance =" ,d,"\t",int(d))
	except KeyboardInterrupt:
		print("CTRL + C KEY PRESSED")
		break
	except Exception as e:
		print(e)