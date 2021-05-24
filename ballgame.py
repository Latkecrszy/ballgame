import pygame, random
from pygame.locals import RESIZABLE

pygame.init()

win = pygame.display.set_mode((1500, 700), RESIZABLE)
font = pygame.font.SysFont('comicsans', 30, True)
pygame.display.set_caption("Ball Game")
air_resistance = 1.05
RECT_HEIGHT = 50
RECT_WIDTH = 140
vert_rect_points = {1: [], 2: [(600, 540), (600, 380), (600, 120)], 3: []}
horiz_rect_points = {1: [], 2: [],
                     3: [(200, 550), (400, 400), (600, 250), (800, 100), (1000, 250), (1200, 400), (300, 250)]}
tri_points = {1: [(700, 690)], 2: [],
              3: [(400, 690), (500, 690), (600, 690), (700, 690), (800, 690), (900, 690), (1000, 690), (1100, 690),
                  (1200, 690), (800, 400)]}
win_points = {1: (1340, 680), 2: (1340, 680), 3: (1340, 680)}
jump_points = {1: [], 2: [(450, 690)], 3: []}
coin_points = {'gold': {
    1: [],
    2: [(625, 320)],
    3: [(865, 220)]
},
    'silver': {
    1: [(735, 500)],
    2: [(625, 100)],
    3: [(870, 75)]
    }}
collected_coins = {'gold': {1: [], 2: [], 3: []}, 'silver': {1: [], 2: [], 3: []}}
level = 1
in_shop = False
shop = {'Orange Ball': {'price': 10, 'description': 'Make your ball orange!'},
        'Yellow Ball': {'price': 10, 'description': 'Make your ball yellow!'}}


class Object:
    def __init__(self, mass: int, height: int, length: int, start: int):
        self.posy = 0
        self.posx = start
        self.vely = 0
        self.velx = 0
        self.mass = mass
        self.height = height
        self.length = length
        self.jumped_for = 0
        self.coins = 0


def draw_tri(coors):
    return (coors[0], coors[1]), (coors[0] + 70, coors[1]), (coors[0] + 35, coors[1] - 60)


def gravity(obj: Object):
    obj.vely += obj.mass / 90


def reset(obj: Object):
    obj.posx = 100
    obj.posy = 650
    obj.vely, obj.velx = 0, 0
    obj.jumped_for = 0
    obj.coins -= len(collected_coins['gold'][level])+len(collected_coins['silver'][level])
    collected_coins['gold'][level] = []
    collected_coins['silver'][level] = []


objects = [Object(100, 20, 20, 30)]
mainLoop = True
while mainLoop:
    pygame.time.delay(10)
    win.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False
    keys = pygame.key.get_pressed()
    if not in_shop:
        for ball in objects:
            if keys[pygame.K_LEFT]:
                ball.velx -= 3
            if keys[pygame.K_RIGHT]:
                ball.velx += 3
            if ball.posy > 690 - ball.height:
                ball.posy = 690 - ball.height
                ball.vely -= int(ball.vely * 1.5) - 0.001
                ball.jumped_for = 0
            elif ball.posy < ball.height:
                ball.posy = ball.height + 50
                ball.vely *= -0.35
            if keys[pygame.K_SPACE]:
                if ball.jumped_for < 4:
                    ball.vely -= 5.7
                    ball.jumped_for += 1
            if ball.posx > 1500 - ball.length:
                ball.velx *= -1
                ball.velx -= 1
                ball.posx = 1500 - ball.length
                ball.jumped_for = 0
            elif ball.posx < ball.length:
                ball.velx *= -1
                ball.velx -= 1
                ball.posx = ball.length
                ball.jumped_for = 0
            ball.posx += ball.velx
            ball.velx /= air_resistance + (ball.mass / 2000)
            for rect in horiz_rect_points[level]:
                if rect[1] - ball.height - 20 <= ball.posy <= rect[1] + 20 - ball.height and ball.vely >= 0 and rect[0] - 15 <= ball.posx <= rect[0] + RECT_WIDTH + 15:
                    ball.posy = rect[1] - ball.height
                    ball.vely = 0
                    ball.jumped_for = 0
                elif rect[1] + 10 - ball.height <= ball.posy <= rect[1] + 110 - ball.height and ball.vely <= 0 and rect[0] - ball.length <= ball.posx <= rect[0] + 151:
                    ball.vely *= -1
                elif int(ball.posy) in range(rect[1], rect[1] + RECT_HEIGHT + ball.height):
                    if int(ball.posx) in range(rect[0] - ball.length, rect[0] + 10):
                        ball.posx = rect[0] - ball.length - 10
                        ball.velx *= -0.2
                    elif int(ball.posx) in range(rect[0] + RECT_WIDTH + 1, rect[0] + RECT_WIDTH + 10):
                        ball.posx = rect[0] + RECT_WIDTH
                        ball.velx *= -0.2
                pygame.draw.rect(win, (255, 255, 0), pygame.Rect(rect[0], rect[1], 140, 50))
            for rect in vert_rect_points[level]:
                if int(ball.posy) in range(rect[1] + ball.height, rect[1] + RECT_WIDTH + ball.height):
                    if int(ball.posx) in range(rect[0] - ball.length, rect[0] + 10):
                        ball.posx = rect[0] - ball.length - 10
                        ball.velx *= -0.2
                    elif int(ball.posx) in range(rect[0] + RECT_HEIGHT, rect[0] + RECT_HEIGHT + 20):
                        ball.posx = rect[0] + RECT_HEIGHT
                        ball.velx *= -0.2
                elif rect[0] - ball.length + 1 <= ball.posx <= rect[0] + RECT_HEIGHT + ball.length:
                    if int(ball.posy) in range(rect[1] - ball.height, rect[1] + RECT_WIDTH):
                        ball.posy = rect[1] - ball.height
                        ball.vely = 0
                        ball.jumped_for = 0
                pygame.draw.rect(win, (255, 255, 0), pygame.Rect(rect[0], rect[1], 50, 140))
            for point in jump_points[level]:
                if point[1] - 50 <= ball.posy - ball.height <= point[1] + 50 and point[0] <= ball.posx <= point[0] + 100:
                    ball.vely = -37
                pygame.draw.rect(win, (45, 12, 235), pygame.Rect(point[0], point[1], 100, 20))
            for i, j in {'gold': [(235, 212, 7), 2], 'silver': [(140, 140, 135), 1]}.items():
                for coin in coin_points[i][level]:
                    if coin not in collected_coins[i][level]:
                        if int(ball.posx) - ball.length + 20 in range(coin[0] - 15, coin[0] + 15) and int(ball.posy) in range(
                                coin[1] - 30, coin[1] + 30):
                            collected_coins[i][level].append(coin)
                            ball.coins += j[1]
                        pygame.draw.circle(win, j[0], coin, 15)
                        win.blit(font.render(f"C", 1, (28, 10, 87)), (coin[0] - 8, coin[1] - 8))
            gravity(ball)
            ball.posy += ball.vely
            for tri in tri_points[level]:
                if int(ball.posx) in range(tri[0] - ball.length + 15, tri[0] + 70 + ball.length) and int(
                        ball.posy) in range(tri[1] - ball.height - 10, tri[1]):
                    reset(ball)
                pygame.draw.polygon(win, (0, 255, 255), draw_tri(tri))
            if int(ball.posx) in range(win_points[level][0], win_points[level][0] + 100 + ball.length) and int(
                    ball.posy) in range(win_points[level][1] - ball.height, win_points[level][1] + 100):
                level += 1
                reset(ball)
            pygame.draw.circle(win, (255, 0, 0), (int(ball.posx), int(ball.posy)), ball.height)
            pygame.draw.rect(win, (0, 255, 0), pygame.Rect(win_points[level][0], win_points[level][1], 100, 20))
            win.blit(font.render(f"Coins: {ball.coins}", 1, (255, 255, 255)), (50, 50))
    else:
        shop_win = pygame.Rect(50, 50, 1350, 600)
        pygame.draw.rect(win, (102, 102, 100), shop_win)
        win.blit(font.render(f"Shop:", 1, (255, 255, 255)), (700, 80))
        num = 1
        for name, info in shop.items():
            if num == 1:
                pygame.draw.rect(win, (0, 255, 38), pygame.Rect(100, 120, 350, 500))
                win.blit(font.render(name, 1, (0, 0, 0)), (210, 150))
            else:
                pygame.draw.rect(win, (0, 255, 38), pygame.Rect(200*num+100, 120, 350, 500))
                win.blit(font.render(name, 1, (0, 0, 0)), (200*num+210, 150))

            num += 1

        if pygame.MOUSEBUTTONUP in [event.type for event in pygame.event.get()]:
            pos = pygame.mouse.get_pos()
            print(pos)

    pygame.display.update()

pygame.quit()
