import turtle as trt
import numpy as np
def lrounding (r):
    for i in range(36):
        trt.forward(10+2*r)
        trt.left(10)
def rrounding (r):
    for i in range(36):
        trt.forward(10+2*r)
        trt.right(10)
def eighhht (r):
    lrounding(r);
    rrounding(r);
def  butfl (n):
    for i in range(n):
        eighhht(i)  
    
trt.shape('turtle')
trt.right(90)
trt.speed(2000)
butfl(12)