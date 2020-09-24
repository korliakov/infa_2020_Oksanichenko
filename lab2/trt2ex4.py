from random import randint
import turtle as trt
import numpy as np

trt.shape('turtle')
trt.speed(1000)
steps_of_time_number = 10000
x = randint(-200, 200)
y = randint(-200, 200)
vx = randint(-30, 30)
vy = randint(-30, 30)
ay = -1
dt = 0.1
trt.penup()
trt.goto(x, y)
trt.pendown()
for i in range(steps_of_time_number):
    x += vx * dt
    y += vy * dt + ay * dt ** 2 / 2
    vy += ay * dt
    trt.goto(x, y)
    if x > 250:
        vx = (-1) * vx
    if x < -250:
        vx = (-1) * vx
    if y > 250:
        vy = (-1) * vy
    if y < -250:
        vy = (-1) * vy
