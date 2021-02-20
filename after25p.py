import serial
from Arduino import Arduino
import time
import datetime
import math
import numpy as np
import cursormove
import collections

'''
468 788 -1066
1154 -2474 -4517 
437 568 -850
1154 -2556 -4354
[ 4.72861058e+05 -6.72779119e+02 -6.72418583e-01] 
[ 4.51979781e+05 -6.01231739e+02 -9.61954224e-01]
  '''
#myArd = Arduino("9600",port="COM5" )
earthF1 = np.array([437,568,-850])
earthF2 = np.array([1154,-2556,-4354])

param1 = [ 472861.05,-672.78,-0.6724]
param2 = [ 451979.78,-601.23,-0.962]

###########_________________________________________________________________
a1 = serial.Serial('COM5',baudrate = 9600)
a2 = serial.Serial('COM6',baudrate = 9600)#with button

modearth1 = round(np.linalg.norm(earthF1),4)
modearth2 = round(np.linalg.norm(earthF2),4)

#initializing queue that stores intensity of last n readings
q1 = collections.deque()
q2 = collections.deque()

n =10
i=0
while i<n:
	q1.append(modearth1)
	q2.append(modearth2)
	i+=1

avgn1 = modearth1
avgn2 = modearth2
#check 
print("average set")

#j=0
while True:
	#j+=1
	#print(j)
	d = 0
	d2 =0
	try:
		tdata1 = a1.readline().decode('ascii')
		tdata2 = a2.readline().decode('ascii')
		#print("\nHOLA",tdata1)
		splitted = tdata1.split(',')
		#print(splitted)
		splitted[2] = splitted[2].strip('\n')
		splitted[2] = splitted[2].strip('\r')
		#print(splitted)
		if (len(splitted)==3):
			vec = np.array(list(map(int,splitted)))
			intensity = round(np.linalg.norm(vec-earthF1),4)
			avgn1 = (avgn1*n - q1.popleft() + intensity)/n
			q1.append(intensity)
			d = np.sqrt(param1[0]/(avgn1-param1[1]))-param1[2]
			#d= round(d,4)
			#sqrt(param1[0]/(ans-param[1]))-param1[2]
			###print(vec,vec-earthF1,int(avgn1),"Distance1 =" ,d,"\t",int(d))

		#for second with button
		splitted2 = tdata2.split(',')
		#print(splitted)
		splitted2[2] = splitted2[2].strip('\n')
		splitted2[2] = splitted2[2].strip('\r')
		flag = False
		if(splitted2[2][-1]=="L"):
			flag = True
			splitted2[2]=splitted2[2][:-1]
		#print(splitted)
		if (len(splitted2)==3):
			vec2 = np.array(list(map(int,splitted2)))
			intensity2 = round(np.linalg.norm(vec2-earthF2),4)
			avgn2 = (avgn2*n - q2.popleft() + intensity2)/n
			q2.append(intensity2)
			d2 = np.sqrt(param2[0]/(avgn2-param2[1]))-param2[2]
			#d2= round(d2,4)
			#sqrt(param1[0]/(ans-param[1]))-param1[2]
			###print(vec2,vec2-earthF2,int(avgn2),"Distance2 =" ,d2,"\t",int(d2))
		

		if d>0 and d2>0 and d+d2>12 and d+12>d2 and d2+12>d :
			if flag :
				cursormove.chaap()
			else:
				cursormove.no_chaap()
			d=round(d,2)
			d2=round(d2,2)
			xx = ((d-d2)*(d+d2))/24#0 to 36cm
			yy = 10 - math.sqrt(abs((d**2)-((xx+6)**2)))#0 to 20cm
			cursormove.bhaga_turtle(round(xx,2),round(yy,2))
		print(int(avgn1),int(avgn2),round(d,1),round(d2,1),round(xx,1),round(yy,1),sep = "\t")
	except KeyboardInterrupt:
		print("Try once more...You can do it \n\t CTRL + C KEY PRESSED")
		break
	except Exception as e:
		print(e)
		#j+=1
'''
i=0
xx1 = 0
yy1=0
while i<1000:
	# if myArd.digitalRead(12) == "LOW":
	# 	print("\t\tSHAKALAKA BOOM BOOM\n")
	flag = False
	data1 = a1.readline()
	data2 = a2.readline()
	#print(data)
	i+=1
	#8.71 , 21,12, 123.12
	Nishant2 = 0
	b2 =0
	if (len(data1)>5):
	    Nishant1=str(data1)
	    # if("LOW" in Nishant1):
	    # 	flag =True
	    # else:
	    rece = Nishant1[2:len(Nishant1)-5]
	    if(len(rece) <7):
		    if(rece[-1] =="L"):
		    	Nishant2=float(rece[:-1])
		    	flag =True
		    else :
		    	Nishant2=float(rece)
		    print("Data2: ", rece)

	if (len(data2)>5):
	    b1=str(data2)
	    rece2=b1[2:len(b1)-5]
	    if(len(rece2) <7):
	    	b2=float(rece2)
	    else:
	    	b2=0
	    print("Data1: ", b2)
	if(b2>0 and Nishant2>0):
		d22= Nishant2*Nishant2
		d12 = b2*b2
		xx = (d12-d22+1056)/24#0 to 88cm
		yy = math.sqrt(abs(d22-((xx-50)*(xx-50))))#0 to 38cm
		if(flag):
			cursormove.chaap() 
			cursormove.bhaga_turtle(int(xx),int(yy))
		else:
			cursormove.no_chaap() 
			cursormove.bhaga_turtle(int(xx),int(yy))
		#xx1=xx
		#yy1=yy
		#print(xx,yy)
	time.sleep(0.1)
'''
#print(a1)