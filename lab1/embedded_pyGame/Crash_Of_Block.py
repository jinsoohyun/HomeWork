#coding:utf-8
# draw ball
# draw ball & moving it
# bounce ball
# draw bar
# control bar

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

px = 0
py = 440
p_width = 80
p_height = 10
keys = [False, False]

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Crash_Of_Block')

def drawbar(x, y):
    pygame.draw.rect(screen, WHITE, (px, py, p_width, p_height))

def drawball(x, y, r):
    pygame.draw.circle(screen, WHITE, (int(x), int(y)), r, 0)

def updateObject():
    global bx, by, dx, dy, px, py, p_width, p_height
    bx += dx
    by += dy
    if bx > width or bx < 0:
        dx = dx * (-1)

    if by > height or by < 0:
        dy = dy * (-1)

    if keys[0] == True:
        px -= 5

    if keys[1] == True:
        px += 5

    if px < 0:
        px = 0
    if px + p_width > 640:
        px = width - p_width

def collideCheck():
    global bx, by, dx, dy, px, py, p_width, p_height, p_vel
    # Collision Check - ball & paddle
    if bx > px and bx < px + p_width and by > py:
        #dx *= -1
        dy *= -1


while True:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                keys[0] = True
            elif event.key == K_RIGHT:
                keys[1] = True


        if event.type == pygame.KEYUP:
            if event.key == K_LEFT:
                keys[0] = False
            elif event.key == K_RIGHT:
                keys[1] = False

    updateObject()
    collideCheck()
    drawball(bx, by, radius)
    drawbar(px, py)
    pygame.display.update()
