import pygame
import random

pygame.init()

win = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Pong by Seth")

paddle_1_x = 30
paddle_2_x = 940
paddle_1_y = 30
paddle_2_y = 350
rect_width = 30
rect_height = 110
rect_vel = 3
ball_vel_y = random.choice([-3, 3])
ball_vel_x = random.choice([-5, 5])
ball_x = 150
ball_y = 150
ball_width = 20
ball_height = 20
ball_2_vel_y = random.choice([-5, 5])
ball_2_vel_x = random.choice([-3, 3])
ball_2_x = 570
ball_2_y = 370

SCREENWIDTH, SCREENHEIGHT = 1000, 700
font = pygame.font.SysFont('comicsans', 30, True)
playerOneScore = 0
playerTwoScore = 0

mainLoop = True
while mainLoop:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False

    keys = pygame.key.get_pressed()
    """if keys[pygame.K_LEFT] and paddle_1_x > rect_vel-5:
        paddle_1_x -= rect_vel
    if keys[pygame.K_RIGHT] and paddle_1_x < SCREENWIDTH - rect_width - rect_vel:
        paddle_1_x += rect_vel"""
    if keys[pygame.K_s] and paddle_1_y < SCREENHEIGHT - rect_height - rect_vel:
        paddle_1_y += rect_vel
    if keys[pygame.K_w] and paddle_1_y > rect_vel - 5:
        paddle_1_y -= rect_vel
    if keys[pygame.K_DOWN] and paddle_2_y < SCREENHEIGHT - rect_height - rect_vel:
        paddle_2_y += rect_vel
    if keys[pygame.K_UP] and paddle_2_y > rect_vel - 5:
        paddle_2_y -= rect_vel

    if ball_y > 700:
        ball_y = 700
        ball_vel_y *= -1
    elif ball_y < 0:
        ball_y = 0
        ball_vel_y *= -1
    if ball_x > 1000:
        playerOneScore += 1
        ball_vel_x *= -1
        ball_x = 500
        ball_y = 350
    elif ball_x < 0:
        playerTwoScore += 1
        ball_vel_x *= -1
        ball_x = 500
        ball_y = 350
    if ball_2_y > 700:
        ball_2_y = 700
        ball_2_vel_y *= -1
    elif ball_2_y < 0:
        ball_2_y = 0
        ball_2_vel_y *= -1
    if ball_2_x > 1000:
        playerOneScore += 1
        ball_2_vel_x *= -1
        ball_2_x = 500
        ball_2_y = 350
    elif ball_2_x < 0:
        playerTwoScore += 1
        ball_2_vel_x *= -1
        ball_2_x = 500
        ball_2_y = 350
    if ball_x in range(ball_2_x, ball_2_x - 10) and ball_y in range(ball_2_y - 10, ball_2_y):
        ball_vel_x *= -1
        ball_2_vel_x *= -1

    if ball_x in range(paddle_1_x, paddle_1_x + 50) and ball_y in range(paddle_1_y, paddle_1_y + 110):
        ball_vel_x *= -1
    if ball_x in range(paddle_2_x - 10, paddle_2_x + 10) and ball_y in range(paddle_2_y, paddle_2_y + 110):
        ball_vel_x *= -1
    if ball_2_x in range(paddle_1_x, paddle_1_x + 50) and ball_2_y in range(paddle_1_y, paddle_1_y + 110):
        ball_2_vel_x *= -1
    if ball_2_x in range(paddle_2_x - 10, paddle_2_x + 10) and ball_2_y in range(paddle_2_y, paddle_2_y + 110):
        ball_2_vel_x *= -1
    ball_x += ball_vel_x
    ball_y += ball_vel_y
    ball_2_x += ball_2_vel_x
    ball_2_y += ball_2_vel_y
    win.fill((0, 0, 0))
    text = font.render(f"Player one: {playerOneScore}               Player two: {playerTwoScore}", 1, (255, 0, 0))
    win.blit(text, (300, 40))
    pygame.draw.rect(win, (0, 255, 0), (paddle_1_x, paddle_1_y, rect_width, rect_height))
    pygame.draw.rect(win, (0, 0, 255), (paddle_2_x, paddle_2_y, rect_width, rect_height))
    pygame.draw.circle(win, (255, 0, 0), (ball_x, ball_y), 20)
    pygame.draw.circle(win, (255, 255, 0), (ball_2_x, ball_2_y), 20)
    pygame.display.update()

pygame.quit()
