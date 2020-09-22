import turtle as trt
import numpy as np
def star (n,r):
    a = r*2*np.cos(np.pi/n)
    alpha = 180*(1/n)
    trt.penup()
    trt.forward(r)
    trt.pendown()
    trt.left(180)
    trt.right(alpha/2)
    for i in range(n):
        trt.forward(a)
        trt.left(180)
        trt.right(alpha)
    

    
trt.shape('turtle')
trt.speed(10)

star(5,100)
trt.penup()
trt.forward(300)
trt.pendown()
star(11,100)