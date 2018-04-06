#coding:utf-8
import pygame, sys
from pygame.locals import *

pygame.init()
G_screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Crash of Block')

BLACK   = ( 0,  0,  0)
WHITE   = (255,255,255)
RED     = (255, 0,  0)
GREEN   = ( 0,255,  0)
BLUE    = ( 0,  0,255)

def drawball(x, y, r):
    pygame.draw.circle(G_screen, WHITE, (x, y), r, 0)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    drawball(300, 300, 10)
    pygame.display.update()
