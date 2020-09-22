import turtle as trt
import turtle
import numpy as np
from random import *
N = 50
def write1num (i):
    B = ['wrzero','wrone','wrfour','wrseven','wrfour','wrfour','wrfour','wrseven']
    s = B[i]+'()'
    eval(s)

        
def wrzero ():
    wrrd('C:\Something\Laby_po_pitonu\lab2\wrzero.txt')
def wrone ():
    wrrd('C:\Something\Laby_po_pitonu\lab2\wrone.txt')
def wrfour ():
    wrrd('C:\Something\Laby_po_pitonu\lab2\wrfour.txt')
def wrseven ():
    wrrd('C:\Something\Laby_po_pitonu\lab2\wrseven.txt')
def wrrd (s):
    inp = open(s, 'r')
    S1 = inp.readlines()
    for i in range(len(S1)):
        S1[i].rstrip()
        eval(S1[i])
    inp.close()
def writenum (s):
    A = list(map(int, s))
    turtle.penup()
    trt.left(180)
    trt.forward(1.5*N*(len(A)/2))
    trt.right(180)
    trt.pendown()
    for i in range(len(A)):
        write1num(int(A[i]))
      
turtle.shape('turtle')
writenum("141700")
#writenum("141700")

