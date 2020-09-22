import turtle as trt
import numpy as np
def n_fig (n):
    for i in range(3,n,1):
        trt.penup()
        trt.forward(10)
        trt.pendown()
        n_ugol(i)
def n_ugol (n):
    aalpha = 180-((n-2)/n)*180
    a = (10*n-7)*2*np.sin(np.pi/n)
    trt.left(90)
    trt.left(aalpha/2)
    for i in range(n):
        trt.forward(a)
        trt.left(aalpha)
    trt.right(aalpha/2)
    trt.right(90)    
trt.shape('turtle')
trt.speed(7)
n_fig(20)