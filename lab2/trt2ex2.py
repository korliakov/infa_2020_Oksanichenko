import turtle as trt
import numpy as np
from random import *
N = 50

def write1num (i):
    B = ['wrzero','wrone','wrfour','wrseven','wrfour','wrfour','wrfour','wrseven']
    s = B[i]+'()'
    eval(s)
    
        
def wrzero ():
    trt.forward(N)
    trt.left(90)
    trt.forward(2*N)
    trt.left(90)
    trt.forward(N)
    trt.left(90)
    trt.forward(2*N)
    trt.left(90)
    trt.penup()
    trt.forward(1.5*N)
    trt.pendown()
def wrone ():
    trt.penup()
    trt.forward(N)
    trt.pendown()
    trt.left(90)
    trt.forward(2*N)
    trt.left(135)
    trt.forward(1.4*N)
    trt.penup()
    trt.right(180)
    trt.forward(1.4*N)
    trt.right(135)
    trt.forward(2*N)
    trt.left(90)
    trt.forward(N/2)
    trt.pendown()
def wrfour ():
    trt.penup()
    trt.forward(N)
    trt.pendown()
    trt.left(90)
    trt.forward(2*N)
    trt.left(180)
    trt.forward(N)
    trt.right(90)
    trt.forward(N)
    trt.right(90)
    trt.forward(N)
    trt.penup()
    trt.right(180)
    trt.forward(N)
    trt.left(90)
    trt.forward(N)
    trt.right(90)
    trt.forward(N)
    trt.left(90)
    trt.forward(N/2)
    trt.pendown()
def wrseven ():
    trt.left(90)
    trt.forward(N)
    trt.penup()
    trt.forward(N)
    trt.pendown()
    trt.right(90)
    trt.forward(N)
    trt.right(135)
    trt.forward(np.sqrt(2)*N)
    trt.left(180)
    trt.penup()
    trt.forward(np.sqrt(2)*N)
    trt.right(135)
    trt.forward(2*N)
    trt.left(90)
    trt.forward(N/2)
    trt.pendown()
def writenum (s):
    A = list(map(int, s))
    
    trt.penup()
    trt.left(180)
    trt.forward(1.5*N*(len(A)/2))
    trt.right(180)
    trt.pendown()
    for i in range(len(A)):
        write1num(int(A[i]))
      
trt.shape('turtle')
writenum("141700")
#writenum("141700")