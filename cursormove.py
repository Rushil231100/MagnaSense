import time
import pyautogui
pyautogui.FAILSAFE= False
import turtle
#turtle.setworldcoordinates(0, -1080, 1920, 0)
turtle.speed(3)
turtle.pensize(15)
turtle.pencolor("#4400b6")
turtle.st()
# turtle.shape()
scaling= 30 #subject to change
def make_boundry():
	no_chaap()
	turtle.goto(-12*scaling,6*scaling)
	chaap()
	turtle.goto(12*scaling,6*scaling)
	turtle.goto(12*scaling,-6*scaling)
	turtle.goto(-12*scaling,-6*scaling)
	turtle.goto(-12*scaling,6*scaling)

def firse():
	turtle.clear()
	turtle.goto(0,0)

def chaap():
	turtle.down()
def no_chaap():
	turtle.up()

def bhaga_turtle(x,y):

	turtle.goto(x*scaling,y*scaling)
	# x*=1920/36#change
	# y*=-1080/24#change
	# if(x<1920 and y>-1080 and x>0 and y<0):
	# 	turtle.goto(int(x),int(y))

def move_cursor(x,  y):
	x*=1920/88
	y*=1080/50
	if(x<1920 and y<1080):
		pyautogui.dragRel(int(x), int(y), duration = 0) 
		#print(pyautogui.position())
	#pyautogui.click(x, y) 


def click_cursor(x,  y):
	
	x*=1920/88
	y*=1080/50
	if(x<1920 and y<1080):
		pyautogui.moveTo(x, y, duration = 0)
		#print(pyautogui.position())
		pyautogui.click(x, y) 

make_boundry()
# chaap()
# bhaga_turtle(0,0)
#move_cursor(88,50)
#move_cursor(100,200)
#click_cursor(100,100)