import turtle
from random import randint

number_of_turtles = 5
steps_of_time_number = 1000
UX = []
UY = []
UVX = []
UVY = []
ay = -1
dt = 0.3
R = 100

pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]
for j in range(number_of_turtles):
    pool[j].penup()
    pool[j].speed(100)
    UX.append(randint(-200, 200))
    UY.append(randint(-200, 200))
    UVX.append(randint(-30, 30))
    UVY.append(randint(-30, 30))
    pool[j].goto(UX[j], UY[j])
    pool[j].pendown()


for i in range(steps_of_time_number):
    for j in range(number_of_turtles):
        UX[j] += UVX[j]*dt
        UY[j] += UVY[j]*dt + ay*dt**2/2
        UVY[j] += ay*dt
        pool[j].goto(UX[j],UY[j])
        if UX[j]>250 :
            UVX[j] = (-1)*UVX[j]
        if UX[j]<-250 :
            UVX[j] = (-1)*UVX[j]    
        if UY[j]>250 :
            UVY[j] = (-1)*UVY[j]
        if UY[j]<-250 :
            UVY[j] = (-1)*UVY[j]
        for k in range(number_of_turtles):
            if(j!=k):
                r = (UX[j]-UX[k])**2+(UY[j]-UY[k])**2
                if(r<100):
                    UVY[j] = (-1)*UVY[j]
                    UVX[j] = (-1)*UVX[j]
                    UVY[k] = (-1)*UVY[k]
                    UVX[k] = (-1)*UVX[k]
        