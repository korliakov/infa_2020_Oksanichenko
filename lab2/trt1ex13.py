import turtle as trt
import numpy as np
def smround (r,s1):

    trt.color('black')
    trt.width(1)
    trt.penup()
    trt.forward(r)
    trt.left(90)
    trt.pendown()
    a = ((2*np.pi)/36)*r
    trt.color(s1)
    trt.begin_fill()
    for i in range(36):
        trt.forward(a)
        trt.left(10)
    trt.end_fill()
    trt.color('black')
    for i in range(36):
        trt.forward(a)
        trt.left(10)
    trt.penup()
    trt.left(90)
    trt.forward(r)
    trt.pendown()
    trt.left(180)

def nose (r):
    trt.color('green')
    trt.width(5)
    trt.pendown()
    trt.left(90)
    trt.forward(r/2)
    trt.left(180)
    trt.forward(r)
    trt.left(180)
    trt.forward(r/2)
    
    trt.color('black')
    trt.width(1)
    
    

def mouth (r):
    trt.right(45)
    trt.penup()
    trt.forward(50)
    trt.pendown()
    trt.right(90)
    a = ((2*np.pi)/36)*r
    trt.color('red')
    trt.width(5)
    for i in range(18):
        trt.forward(a/2)
        trt.right(5)
    trt.right(90)
    trt.penup()
    trt.forward(50)
    trt.pendown()
    trt.right(45)
    trt.color('black')
    trt.width(1)
    
trt.shape('turtle')
trt.speed(100)
smround(100,'yellow')
trt.left(135)
trt.penup()
trt.forward(50)
trt.pendown()
smround(15,'blue')
trt.right(180)
trt.penup()
trt.forward(50)
trt.pendown()
trt.left(90)
trt.penup()
trt.forward(50)
trt.pendown()
smround(15,'blue')
trt.right(180)
trt.penup()
trt.forward(50)
trt.pendown()
trt.left(135)


mouth(50)
nose(30)
