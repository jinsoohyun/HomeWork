#coding:utf-8
# draw ball
# draw ball & moving it
# bounce ball
# draw bar
# control bar
# draw block
# check collision block & ball
# veiw score

import pygame, sys, math, random
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
tAngle = 45

px = 0
py = 440
p_vel = 10
p_width = 80
p_height = 10

bricks_cols = 3
bricks_rows = 7
brickWidth = 75
brickHeight = 20
brickPadding = 10
brickOffsetTop = 40
brickOffsetLeft = 30

score = 1000

keys = [False, False]
bricks = []

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Crash_Of_Block')

# font
fontObj = pygame.font.SysFont('Courier', 20)


def bricksInit():
    global bricks_cols, bricks_rows, brickWidth, brickHeight, brickPadding, brickOffsetTop, brickOffsetLeft

    for r in range(bricks_rows):
        for c in range(bricks_cols):
            state = 1
            x = brickOffsetLeft + r*(brickPadding + brickWidth)
            y = brickOffsetTop + c*(brickPadding + brickHeight)
            oneBrick = [x, y, state]
            bricks.append(oneBrick)

    print(bricks)

def drawBricks():
    global bricks_cols, bricks_rows, brickWidth, brickHeight, brickPadding, brickOffsetTop, brickOffsetLeft
    for b in bricks:
        if b[2] == 1 :
            pygame.draw.rect(screen, GREEN, (b[0], b[1],brickWidth, brickHeight))



def drawbar(x, y):
    pygame.draw.rect(screen, WHITE, (px, py, p_width, p_height))

def drawball(x, y, r):
    pygame.draw.circle(screen, WHITE, (int(x), int(y)), r, 0)

def updateObject():
    global bx, by, dx, dy, px, py, p_width, p_height, p_vel, tAngle

    bx += dx
    #by += dy
    by += int( round( math.tan(math.radians(tAngle)) * dx ) ) * -1
    #print "%r %r" % (bx,  by)

    if bx > width or bx < 0:
        dx = dx * (-1)
        tAngle = 180 - tAngle

    if by > height or by < 0:
        #dy = dy * (-1)
        tAngle = 180 - tAngle


    if keys[0] == True:
        px -= p_vel

    if keys[1] == True:
        px += p_vel

    if px < 0:
        px = 0
    if px + p_width > 640:
        px = width - p_width

def collideCheck():
    global bx, by, dx, dy, px, py, p_width, p_height, p_vel
    global bricks_cols, bricks_rows, brickWidth, brickHeight, brickPadding, brickOffsetTop, brickOffsetLeft, tAngle
    global score

    # Collision Check - ball & paddle
    if bx > px and bx < px + p_width and by > py:
        #dx *= -1
        #dy *= -1
        tAngle = 180 - tAngle + random.randint(-20, 20)

    # check the block collision
    for b in bricks:
        if bx > b[0] and bx < b[0]+brickWidth and by > b[1] and by < b[1]+brickHeight  and b[2] == 1:  #state == 1일 때에만 체크
            b[2] = 0
            #dy *= -1
            tAngle = 180 - tAngle
            score += 100



def drawScore(screen, scoreView):
    scoreView = fontObj.render(str(score), True, WHITE, BLACK)
    scoreRect = scoreView.get_rect()
    scoreRect.topleft = (10, 10)
    screen.blit(scoreView, scoreRect)


def scoreInit():
    global fontObj, score
    score = 1000
    fontObj = pygame.font.SysFont('Courier', 20)
    scoreView = fontObj.render('10000000', True, WHITE, BLACK)
    #scoreRect = scoreView.get_rect()
    #scoreRect.center = (200, 50)
    return scoreView


def main():
    bricksInit()
    scoreView = scoreInit()

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
        drawBricks()
        drawball(bx, by, radius)
        drawbar(px, py)
        drawScore(screen, scoreView)
        pygame.display.update()

if __name__ == '__main__':
    main()
