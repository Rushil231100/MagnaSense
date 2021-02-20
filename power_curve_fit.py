import numpy as np
from scipy import optimize
from matplotlib import pyplot as plt

x = np.array([4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,30,100])
# x=1/x**2
# print(x)

#y1 = np.array([11950,7350,5350,3910,3070,2410,1910,1530,1240,1060,870,740,620,540,480,420,360,310,160,100])
#y2 = np.array([12700,8090,5760,4230,3245,2550,2000,1610,1290,1090,895,760,640,545,470,420,370,310,150,100])

y1 = np.array([41480,25650,16640,11510,7970,5560,3970,3110,2440,1990,1580,1270,1070,910,770,630,540,470,420,380,320,160,2000])
y2 = np.array([48170,27120,17880,13280,8190,5700,4230,3290,2595,2070,1640,1340,1110,950,790,670,580,510,440,400,340,150,2000])

#y1 = np.array([,100])
#y2 = np.array([,100])

x1 = np.linspace(4,30,num=1000)
def test(x,a,b,c):
	return a/((x+c)**2)+b

param1,param_cov = optimize.curve_fit(test,x,y1,p0=[530000,0,0])
param2,param_cov = optimize.curve_fit(test,x,y2,p0=[530000,0,0])
ans1 = param1[0]/((x1+param1[2])**2)+param1[1] 
ans2 = param2[0]/((x1+param2[2])**2)+param2[1]
#[ 5.22407734e+05 -1.04617181e+03 -1.19532298e+00]
#sqrt(param1[0]/(ans-param[1]))-param1[2]
print(param1,param2)

plot1 = plt.figure(1)
plt.plot(x[:-1], y1[:-1], 'o', color ='red', label ="data") 
plt.plot(x1[:-1], ans1[:-1], '--', color ='blue', label ="optimized data") 


plot2 = plt.figure(2)
plt.plot(x[:-1], y2[:-1], 'o', color ='red', label ="data2") 
plt.plot(x1[:-1], ans2[:-1], '--', color ='blue', label ="optimized data2") 

plt.legend()
plt.show() 
