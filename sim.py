import pygame, random
from pygame.locals import RESIZABLE
pygame.init()

win = pygame.display.set_mode((1500, 700), RESIZABLE)
pygame.display.set_caption("Ball Game")
air_resistance = 1.02
gap = random.randint(0, 600)
rect_points = {1: [(200, 550), (400, 400), (600, 250), (800, 100), (1000, 250), (1200, 400), (300, 250)]}
tri_points = {1: [(400, 690), (500, 690), (600, 690), (700, 690), (800, 690), (900, 690), (1000, 690), (1100, 690), (1200, 690)]}
win_points = {1: (1340, 680)}
level = 1


def draw_tri(coors):
    return (coors[0], coors[1]), (coors[0]+50, coors[1]), (coors[0]+25, coors[1]-45)


class Object:
    def __init__(self, mass: int, height: int, length: int, start: int):
        self.posy = 0
        self.posx = start
        self.vely = 0
        self.velx = 0
        self.mass = mass
        self.height = height
        self.length = length
        self.elasticity = 1.1
        self.jumped_for = 0


def gravity(obj: Object):
    obj.vely += obj.mass/100


objects = [Object(100, 30, 30, 30)]
mainLoop = True
while mainLoop:
    win.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False
    keys = pygame.key.get_pressed()
    for ball in objects:
        if keys[pygame.K_LEFT]:
            ball.velx -= 3
        if keys[pygame.K_RIGHT]:
            ball.velx += 3
        if ball.posy > 690-ball.height:
            ball.posy = 690-ball.height
            ball.vely -= int(ball.vely*1.5)-0.001
            ball.jumped_for = 0
        elif ball.posy < ball.height:
            ball.posy = ball.height+50
            ball.vely *= -0.35
        if keys[pygame.K_SPACE]:
            if ball.jumped_for < 5:
                ball.vely -= 6
                ball.jumped_for += 1
            print(ball.jumped_for)
        if ball.posx > 1500-ball.length:
            ball.velx *= -1
            ball.velx -= 1
            ball.posx = 1500-ball.length
            ball.jumped_for = 0
        elif ball.posx < ball.length:
            ball.velx *= -1
            ball.velx -= 1
            ball.posx = ball.length
            ball.jumped_for = 0
        ball.posx += ball.velx
        ball.velx /= air_resistance+(ball.mass/2000)
        for rect in rect_points[level]:
            if int(ball.posy) in range(rect[1]-20-ball.height, rect[1]+20-ball.height) and ball.vely >= 0 and int(ball.posx) in range(rect[0]-ball.length, rect[0]+151):
                ball.posy = rect[1]-ball.height
                ball.vely = 0
                ball.jumped_for = 0
            elif int(ball.posy) in range(rect[1]+10-ball.height, rect[1]+110-ball.height) and ball.vely <= 0 and int(ball.posx) in range(rect[0]-ball.length, rect[0]+151):
                ball.vely *= -1
            pygame.draw.rect(win, (255, 255, 0), pygame.Rect(rect[0], rect[1], 140, 50))
        gravity(ball)
        ball.posy += ball.vely
        for tri in tri_points[level]:
            if int(ball.posx) in range(tri[0]-ball.length+15, tri[0]+40+ball.length) and int(ball.posy) in range(tri[1]-ball.height-45, tri[1]):
                ball.posx = 100
                ball.posy = 0
                ball.vely = 0
                ball.velx = 0
                ball.jumped_for = 0
            pygame.draw.polygon(win, (0, 255, 255), draw_tri(tri))
        if int(ball.posx) in range(win_points[level][0]-ball.length, win_points[level][0]+100+ball.length) and int(ball.posy) in range(win_points[level][1]-10,  win_points[level][1]+100):
            level += 1
        pygame.draw.circle(win, (255, 0, 0), (int(ball.posx), int(ball.posy)), ball.height)
        pygame.draw.rect(win, (0, 255, 0), pygame.Rect(win_points[level][0], win_points[level][1], 100, 20))
    pygame.display.update()


pygame.quit()
