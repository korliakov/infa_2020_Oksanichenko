import turtle as trt
import numpy as np
def lrounding ():
    for i in range(36):
        trt.forward(10)
        trt.left(10)
def rrounding ():
    for i in range(36):
        trt.forward(10)
        trt.right(10)
def eighhht ():
    lrounding();
    rrounding();
def flower (n):
    for i in range(n):
        eighhht()
        trt.left(360/n)  
    
trt.shape('turtle')
trt.speed(2000)
flower(12)