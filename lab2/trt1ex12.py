import turtle as trt
import numpy as np
def badround1 ():
    for i in range(36):
        trt.forward(10-i*(19/72))
        trt.right(5)
def badround2 ():
    for i in range(36):
        trt.forward(10-(36-i)*(19/72))
        trt.right(5)

def  petlya (n):
    for i in range(n):
        badround1()
        badround2()
    
trt.shape('turtle')
trt.speed(100)
petlya(12)