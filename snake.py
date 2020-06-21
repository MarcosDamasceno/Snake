import pygame
from pygame.locals import *
import random


def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


def texto(msg, cor):
    texto1 = font.render(msg, True, cor)
    fundo.blit(texto1, [LARGURA/2], [ALTURA/2])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
END = 4
VEL = 10
TAIL = 1
QUANT_FRUIT = 0
ALTURA = 400
LARGURA = 400
game = True
fimdejogo = False

pygame.init()
screen = pygame.display.set_mode((ALTURA, LARGURA))
pygame.display.set_caption('Snake')
snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

high_score = 0
score = 0
apple_pos = (random.randint(0, (ALTURA/10)-1)*10,
             random.randint(0, (LARGURA/10)-1)*10)
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))
my_direction = LEFT

clock = pygame.time.Clock()
pygame.display.set_caption(
    'Snake - ' + str(score) + ' Pontos - Nível: ' + str(VEL-10))

while game:
    clock.tick(VEL)
    while fimdejogo:
        screen.fill((255, 255, 255))
        texto('Fim de jogo, para continuar tecle C ou S para sair', ((255, 0, 0)))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                fimdejogo = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    jogo()
                if event.key == pygame.K_s:
                    game = False
                    fimdejogo = False
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT
            if event.key == K_RIGHT and my_direction != LEFT:
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
        apple_pos = (random.randint(0, (ALTURA/10)-1)*10,
                     random.randint(0, (LARGURA/10)-1)*10)
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

    if snake[0][0] == (LARGURA):
        snake[0] = (snake[0][0] - LARGURA, snake[0][1])
    if snake[0][0] == -10:
        snake[0] = (snake[0][0] + LARGURA, snake[0][1])
    if snake[0][1] == (ALTURA):
        snake[0] = (snake[0][0], snake[0][1] - ALTURA)
    if snake[0][1] == -10:
        snake[0] = (snake[0][0], snake[0][1] + ALTURA)

    for corpo in range(1, len(snake), 1):
        if collision(snake[corpo], snake[0]):
            print('colidiu')
            fimdejogo = True

    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()
