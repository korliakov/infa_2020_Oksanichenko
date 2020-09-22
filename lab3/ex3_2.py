import pygame
import numpy as np
from pygame.draw import *


def ang_rect(sc, x0, y0, w, h, angle, color, w1=0):
    x1 = x0 + w * 0.5 * np.cos((np.pi / 180) * angle) - h * 0.5 * np.sin((np.pi / 180) * angle)
    y1 = y0 + h * 0.5 * np.cos((np.pi / 180) * angle) + w * 0.5 * np.sin((np.pi / 180) * angle)
    x2 = x0 - w * 0.5 * np.cos((np.pi / 180) * angle) - h * 0.5 * np.sin((np.pi / 180) * angle)
    y2 = y0 + h * 0.5 * np.cos((np.pi / 180) * angle) - w * 0.5 * np.sin((np.pi / 180) * angle)
    x3 = x0 - w * 0.5 * np.cos((np.pi / 180) * angle) + h * 0.5 * np.sin((np.pi / 180) * angle)
    y3 = y0 - h * 0.5 * np.cos((np.pi / 180) * angle) - w * 0.5 * np.sin((np.pi / 180) * angle)
    x4 = x0 + w * 0.5 * np.cos((np.pi / 180) * angle) + h * 0.5 * np.sin((np.pi / 180) * angle)
    y4 = y0 - h * 0.5 * np.cos((np.pi / 180) * angle) + w * 0.5 * np.sin((np.pi / 180) * angle)
    polygon(sc, color, [(x1, y1), (x2, y2), (x3, y3), (x4, y4)], w1)


def ang_rect2(sc, x0, y0, w, h, angle, num, color, w1=0):
    by = 1
    if num > 1:
        by = -1
    bx = 1
    if num == 1:
        bx = -1
    if num == 2:
        bx = -1
    x0 = x0 - (bx * w * 0.5 * np.cos((np.pi / 180) * angle) - by * h * 0.5 * np.sin((np.pi / 180) * angle))
    y0 = y0 - (by * h * 0.5 * np.cos((np.pi / 180) * angle) + bx * w * 0.5 * np.sin((np.pi / 180) * angle))
    ang_rect(sc, x0, y0, w, h, angle, color, w1)


def poster(sc, x0, y0, w, h, s, back_col, text_col):
    ang_rect(sc, x0, y0, w, h, 0, back_col)
    ang_rect(sc, x0, y0, w, h, 0, BLC, 1)
    f1 = pygame.font.Font(None, 100)
    text1 = f1.render(s, 1, (0, 0, 0))
    place = text1.get_rect(center=(x0, y0))
    sc.blit(text1, place)


def hair(r_head, r_tr, phi, n, x0, y0, sc, color_fill, color_side):
    for i in range(n):
        alpha = -(90 - phi + (2 * phi * i + phi) / n)
        x1 = int(x0 + r_head * np.cos((np.pi / 180) * alpha) + np.sqrt(3) * 0.5 * r_tr * np.sin((np.pi / 180) * alpha))
        y1 = int(y0 + r_head * np.sin((np.pi / 180) * alpha) - np.sqrt(3) * 0.5 * r_tr * np.cos((np.pi / 180) * alpha))
        x2 = int(x0 + r_head * np.cos((np.pi / 180) * alpha) - np.sqrt(3) * 0.5 * r_tr * np.sin((np.pi / 180) * alpha))
        y2 = int(y0 + r_head * np.sin((np.pi / 180) * alpha) + np.sqrt(3) * 0.5 * r_tr * np.cos((np.pi / 180) * alpha))
        x3 = int(x0 + (r_head + r_tr * 1.5) * np.cos((np.pi / 180) * alpha))
        y3 = int(y0 + (r_head + r_tr * 1.5) * np.sin((np.pi / 180) * alpha))
        polygon(sc, color_fill, [(x1, y1), (x2, y2), (x3, y3)])
        polygon(sc, color_side, [(x1, y1), (x2, y2), (x3, y3)], 1)


def mouth(x0, y0, h_mouth, w_mouth, color, sc):
    x1 = x0 + w_mouth / 2
    y1 = y0
    x2 = x0 - w_mouth / 2
    y2 = y0
    x3 = x0
    y3 = y0 + h_mouth
    polygon(sc, color, [(x1, y1), (x2, y2), (x3, y3)])
    polygon(sc, BLC, [(x1, y1), (x2, y2), (x3, y3)], 1)


def eye(x0, y0, r_pup_x, r_pup_y, r_eye_x, r_eye_y, dy_pup, color_pup, color_eye, sc):
    ellipse(sc, color_eye, [x0 - r_eye_x, y0 - r_eye_y, 2 * r_eye_x, 2 * r_eye_y])
    ellipse(sc, BLC, [x0 - r_eye_x, y0 - r_eye_y, 2 * r_eye_x, 2 * r_eye_y], 1)
    ellipse(sc, color_pup, [x0 - r_pup_x, y0 - r_pup_y + dy_pup, 2 * r_pup_x, 2 * r_pup_y])


def nose(x0, y0, r_nose, color_nose, sc):
    x1 = x0
    y1 = y0 + r_nose
    x2 = x0 + int(np.cos(np.pi / 6) * r_nose)
    y2 = y0 - int(np.sin(np.pi / 6) * r_nose)
    x3 = x0 - int(np.cos(np.pi / 6) * r_nose)
    y3 = y0 - int(np.sin(np.pi / 6) * r_nose)
    polygon(sc, color_nose, [(x1, y1), (x2, y2), (x3, y3)])
    polygon(sc, BLC, [(x1, y1), (x2, y2), (x3, y3)], 1)


def face(x0, y0, r_nose, y_nose, w_mouth, h_mouth, r_pup_x, r_pup_y, r_eye_x, r_eye_y, dy_pup, x_eye, y_eye, y_mouth, color_mouth,
         color_pup, color_eye, color_nose, sc):
    mouth(x0, y0 + y_mouth, h_mouth, w_mouth, color_mouth, sc)
    eye(x0 - x_eye, y0 - y_eye, r_pup_x, r_pup_y, r_eye_x, r_eye_y, dy_pup, color_pup, color_eye, sc)
    eye(x0 + x_eye, y0 - y_eye, r_pup_x, r_pup_y, r_eye_x, r_eye_y, dy_pup, color_pup, color_eye, sc)
    nose(x0, y0+y_nose, r_nose, color_nose, sc)


def boy_next_door(color_hair, color_eyes, color_t_shirt, size, sc, x0, y0):
    angle_sh = 70
    angle_pl_sh = 40
    circle(sc, color_t_shirt, [int(0.5 * size) + x0, int(1 * size) + y0], int(0.3 * size))
    circle(sc, SKN, [int(0.5 * size) + x0, int(0.6 * size) + y0], int(0.2 * size))
    x1 = int(0.5 * size - 0.3 * size * np.cos((np.pi / 180) * angle_pl_sh)) + x0
    y1 = int(size - 0.3 * size * np.sin((np.pi / 180) * angle_pl_sh)) + y0
    x2 = int(0.5 * size + 0.3 * size * np.cos((np.pi / 180) * angle_pl_sh)) + x0
    y2 = int(size - 0.3 * size * np.sin((np.pi / 180) * angle_pl_sh)) + y0
    A1 = []
    for i in range(5):
        A1.append((x1 + int(0.1 * size) * np.cos((np.pi / 180) * (angle_sh + 73 * i)),
                   y1 - int(0.1 * size) * np.sin((np.pi / 180) * (angle_sh + 73 * i))))

    ang_rect2(sc, x1, y1, int(0.63 * size), int(0.034 * size), +73, 3, SKN)
    ang_rect2(sc, x1, y1, int(0.63 * size), int(0.034 * size), +73, 3, BLC, 1)
    polygon(sc, color_t_shirt, A1)
    polygon(sc, BLC, A1, 1)
    A2 = []
    for i in range(5):
        A2.append((x2 - int(0.1 * size) * np.cos((np.pi / 180) * (angle_sh + 73 * i)),
                   y2 - int(0.1 * size) * np.sin((np.pi / 180) * (angle_sh + 73 * i))))
    ang_rect2(sc, x2, y2, int(0.63 * size), int(0.034 * size), -73, 2, SKN)
    ang_rect2(sc, x2, y2, int(0.63 * size), int(0.034 * size), -73, 2, BLC, 1)
    polygon(sc, color_t_shirt, A2)
    polygon(sc, BLC, A2, 1)
    circle(sc, SKN, [int(0.5 * size - 0.43 * size) + x0, int(0.5 * size - 0.3 * size) + y0], int(0.042 * size))
    circle(sc, BLC, [int(0.5 * size - 0.43 * size) + x0, int(0.5 * size - 0.3 * size) + y0], int(0.042 * size), 1)
    circle(sc, SKN, [int(0.5 * size + 0.43 * size) + x0, int(0.5 * size - 0.3 * size) + y0], int(0.042 * size))
    circle(sc, BLC, [int(0.5 * size + 0.43 * size) + x0, int(0.5 * size - 0.3 * size) + y0], int(0.042 * size), 1)
    hair(int(size * 0.2), int(size * 0.04), 60, 10, int(0.5 * size) + x0, int(0.6 * size) + y0, sc, color_hair, BLC)
    face(int(0.5 * size) + x0, int(0.6 * size) + y0, int(0.02 * size), int(0.02 * size), int(0.23 * size), int(0.08 * size), int(0.012 * size), int(0.009 * size), int(0.048 * size), int(0.045 * size), int(0.005 * size), int(0.065 * size), int(0.045 * size), int(0.06 * size), RED, BLC, color_eyes, BRW,
         sc)


pygame.init()

FPS = 30
SIZE = 800
screen = pygame.display.set_mode((SIZE, SIZE))

WHT = (255, 255, 255)
YLW = (255, 255, 0)
BLC = (0, 0, 0)
RED = (255, 0, 0)
SKN = (220, 185, 180)
ORG = (255, 100, 0)
GRN = (0, 255, 0)
DGN = (35, 133, 0)
BRW = (110, 66, 0)
GBL = (100, 133, 255)
PNK = (233, 0, 237)
GGR = (171, 191, 171)
LOR = (255, 215, 0)
screen.fill(WHT)
boy_next_door(PNK, GBL, ORG, SIZE, screen, 0, 0)
poster(screen, int(SIZE * 0.5), int(SIZE * 0.17), int(SIZE * 0.98), int(SIZE * 0.09), "PYTHON is AMAIZING", GRN, BLC)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
