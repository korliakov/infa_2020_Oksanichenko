import turtle as trt
import numpy as np
from random import *
def brmove ():
    for i in range(36):
        trt.forward(randint(5,100))
        if randint(0,10)>5 :
            trt.left(randint(0,180))
        else:
            trt.right(randint(0,180))
      
trt.shape('turtle')
while(2>1):
    brmove()