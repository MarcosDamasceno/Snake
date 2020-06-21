import pygame
import random
from pygame.locals import *


def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


def randonize:
    return (random.randint(0, 40)*10, random.randint(0, 40)*10)


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
END = 4
VEL = 10
TAIL = 1
QUANT_FRUIT = 0

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

high_score = 0
score = 0
apple_pos = randonize
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))
my_direction = LEFT

clock = pygame.time.Clock()
pygame.display.set_caption(
    'Snake - ' + str(score) + ' Pontos - Nível: ' + str(VEL-10))

while True:
    clock.tick(VEL)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT
            if event.key == K_q:
                pygame.quit()
            if event.key == K_k:
                my_direction = END

    if collision(snake[0], apple_pos):
        for x in range(TAIL):
            snake.append((0, 0))
        if QUANT_FRUIT < 10:
            TAIL = 1
            apple.fill((255, 0, 0))
            QUANT_FRUIT = QUANT_FRUIT + 1
        else:
            TAIL = 5
            apple.fill((100, 100, 100))
            QUANT_FRUIT = 0
            VEL = VEL + 1
        apple_pos = randonize
        score = score + 10
        pygame.display.set_caption(
            'Snake - ' + str(score) + ' Pontos - Nível: ' + str(VEL-10))

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    if my_direction == END:
        snake[0] = (snake[0][0], snake[0][1])

    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()
