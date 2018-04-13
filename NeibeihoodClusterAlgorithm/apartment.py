#-*- coding:UTF-8 -*-

from graphics import *

def drawSquare(point,win,side):
	point1=Point(point.getX()-side/2.0,point.getY()-side/2.0)
	point2=Point(point.getX()+side/2.0,point.getY()+side/2.0)
	square=Rectangle(point1,point2)
	square.setFill("black")
	square.draw(win)
	return square


side=float(input("please input the side:"))
print "side is:",side
print ""
increasement=float(input("please input the increasement:"))
print "increasement is:",increasement
print ""
win=GraphWin("Apartment Algorithm",150,150)
win.setCoords(-30,-30,120,120)

point_list=[Point(10,20),Point(15,23),Point(24,50),Point(5,20),Point(11,12),
			Point(7,13),Point(42,30),Point(54,52),Point(63,70),Point(70,52),
			Point(88,70),Point(72,90),Point(61,77),Point(55,82),Point(42,62),
			Point(57,32),Point(68,51),Point(49,72),Point(73,50),Point(76,72)]

square_list=[0]*20

choose=int(input("do you want to do more? 1/0"))
while choose!=0:
	for i in range(len(point_list)):
		square_list[i]=drawSquare(point_list[i],win,side)

	choose=int(input("do you want to do more? 1/0"))
	if choose!=0:
		side=side+increasement
		for j in range(len(square_list)):
			square_list[j].undraw()

win.getMouse()
win.close()