#coding:utf-8
# draw ball
# draw ball & moving it

import pygame, sys
from pygame.locals import *

BLACK   = ( 0,  0,  0)
WHITE   = (255,255,255)
RED     = (255, 0,  0)
GREEN   = ( 0,255,  0)
BLUE    = ( 0,  0,255)

width = 640
height = 480
radius = 10
bx = width / 2
by = height / 2
dx = 1
dy = 1

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Crash_Of_Block')

def drawball(x, y, r):
    pygame.draw.circle(screen, WHITE, (int(x), int(y)), r, 0)

while True:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    bx += dx
    by += dy
    drawball(bx, by, radius)
    pygame.display.update()
