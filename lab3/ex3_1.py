import pygame
import numpy as np
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))

WHT = (255, 255, 255)
YLW = (255, 255, 0)
BLC = (0, 0, 0)
RED = (255, 0, 0)
screen.fill(WHT)
circle(screen, YLW, [300, 300], 200)
circle(screen, BLC, [300, 300], 200, 1)
circle(screen, BLC, [370, 250], 20)  # eyes
circle(screen, RED, [370, 250], 10)
circle(screen, BLC, [230, 250], 30)
circle(screen, RED, [230, 250], 10)
x1e1 = 370 - np.sin((np.pi / 180) * 30) * 20
y1e1 = 250 - np.cos((np.pi / 180) * 30) * 20
x2e1 = x1e1 - np.cos((np.pi / 180) * 30) * 40
y2e1 = y1e1 + np.sin((np.pi / 180) * 30) * 40
x3e1 = x2e1 - np.sin((np.pi / 180) * 30) * 10
y3e1 = y2e1 - np.cos((np.pi / 180) * 30) * 10
x4e1 = x3e1 + np.cos((np.pi / 180) * 30) * 80
y4e1 = y3e1 - np.sin((np.pi / 180) * 30) * 80
x5e1 = x4e1 + np.sin((np.pi / 180) * 30) * 10
y5e1 = y4e1 + np.cos((np.pi / 180) * 30) * 10
x6e1 = x5e1 - np.cos((np.pi / 180) * 30) * 40
y6e1 = y5e1 + np.sin((np.pi / 180) * 30) * 40
Eyebrown1 = [(x1e1, y1e1), (x2e1, y2e1), (x3e1, y3e1), (x4e1, y4e1), (x5e1, y5e1), (x6e1, y6e1)]

x1e2 = 230 + np.sin((np.pi / 180) * 30) * 30
y1e2 = 250 - np.cos((np.pi / 180) * 30) * 30
x2e2 = x1e2 + np.cos((np.pi / 180) * 30) * 50
y2e2 = y1e2 + np.sin((np.pi / 180) * 30) * 50
x3e2 = x2e2 + np.sin((np.pi / 180) * 30) * 15
y3e2 = y2e2 - np.cos((np.pi / 180) * 30) * 15
x4e2 = x3e2 - np.cos((np.pi / 180) * 30) * 100
y4e2 = y3e2 - np.sin((np.pi / 180) * 30) * 100
x5e2 = x4e2 - np.sin((np.pi / 180) * 30) * 15
y5e2 = y4e2 + np.cos((np.pi / 180) * 30) * 15
x6e2 = x5e2 + np.cos((np.pi / 180) * 30) * 50
y6e2 = y5e2 + np.sin((np.pi / 180) * 30) * 50
Eyebrown2 = [(x1e2, y1e2), (x2e2, y2e2), (x3e2, y3e2), (x4e2, y4e2), (x5e2, y5e2), (x6e2, y6e2)]
polygon(screen, BLC, Eyebrown1)
polygon(screen, BLC, Eyebrown2)
x1 = 200
y1 = 400
w = 200
h = 20
rect(screen, BLC, (x1, y1, w, h))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
