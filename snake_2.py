from random import randint
import pygame
from pygame.locals import *
import tkinter as tk
from tkinter.font import Font

branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

try:
    pygame.init()

except:
    print('O modulo pygame não foi inicializado com sucesso')

LARGURA = 640
ALTURA = 480
TAMANHO = 10

relogio = pygame.time.Clock()
fundo = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Snake')
font = pygame.font.SysFont(None, 25)
fonte = pygame.font.SysFont()


# def collision(c1, c2):
#     return (c1[0] == c2[0]) and (c1[1] == c2[1])


# def randomize():
#     return (random.randint(0, LARGURA/10)*10, random.randint(0, ALTURA/10)*10)


def texto(msg, cor):
    texto1 = font.render(msg, True, cor)
    fundo.blit(texto1, [LARGURA/2], [ALTURA/2])


def cobra(CobraXY):
    for XY in CobraXY:
        pygame.draw.rect(fundo, preto, [XY[0], XY[1], TAMANHO, TAMANHO])


def maca(pos_x, pos_y):
    pygame.draw.rect(fundo, vermelho, [pos_x, pos_y, TAMANHO, TAMANHO])


def jogo():
    sair = True
    fimdejogo = False
    pos_x = randint(0, (LARGURA - TAMANHO)/10)*10
    pos_y = randint(0, (ALTURA - TAMANHO)/10)*10
    maca_x = randint(0, (LARGURA - TAMANHO)/10)*10
    maca_y = randint(0, (ALTURA - TAMANHO)/10)*10
    velocidade_x = 0
    velocidade_y = 0
    CobraXY = []
    CobraComp = 1
    while sair:
        while fimdejogo:
            fundo.fill(branco)
            texto('Fim de jogo, para continuar tecle C ou S para sair', vermelho)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    fimdejogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        jogo()
                    if event.key == pygame.K_s:
                        sair = False
                        fimdejogo = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != TAMANHO:
                    velocidade_y = 0
                    velocidade_x = -TAMANHO
                if event.key == pygame.K_RIGHT and velocidade_x != -TAMANHO:
                    velocidade_y = 0
                    velocidade_x = TAMANHO
                if event.key == pygame.K_UP and velocidade_y != TAMANHO:
                    velocidade_x = 0
                    velocidade_y = -TAMANHO
                if event.key == pygame.K_RIGHT and velocidade_y != -TAMANHO:
                    velocidade_x = 0
                    velocidade_y = TAMANHO
        fundo.fill(branco)
        pos_x += velocidade_x
        pos_y += velocidade_y

        CobraInicio = []
        CobraInicio.append(pos_x)
        CobraInicio.append(pos_y)
        CobraXY.append(CobraInicio)
        if len(CobraXY) > CobraComp:
            del CobraXY[0]

        if any(Bloco == CobraInicio for Bloco in CobraXY[:-1]):
            fimdejogo = True

        cobra(CobraXY)
        if pos_x == maca_x and pos_y == maca_y:
            maca_x = randint(0, (LARGURA-TAMANHO)/10)*10
            maca_y = randint(0, (ALTURA-TAMANHO)/10)*10
            CobraComp = + 1

        maca(maca_x, maca_y)
        pygame.display.update()
        relogio.tick(15)

        # VERSAO TELETRANSPORTE
        # if pos_x > LARGURA:
        #     pos_x = 0
        # if pos_x < 0:
        #     pos_x=LARGURA-TAMANHO
        # if pos_y > ALTURA:
        #     pos_y = 0
        # if pos_y < 0:
        #     pos_y=ALTURA-TAMANHO
        # VERSAO FIM DE JOGO
        if pos_x > LARGURA:
            fimdejogo = False
        if pos_x < 0:
            fimdejogo = False
        if pos_y > ALTURA:
            fimdejogo = False
        if pos_y < 0:
            fimdejogo = False

# jogo()
# pygame.quit()
# PRIMEIRA VERSÃO DO JOGO

# UP = 0
# RIGHT = 1
# DOWN = 2
# LEFT = 3
# END = 4
# VEL = 10
# TAIL = 1
# QUANT_FRUIT = 0

# pygame.init()

# snake = [(200, 200), (210, 200), (220, 200)]
# snake_skin = pygame.Surface((10, 10))
# snake_skin.fill((255, 255, 255))

# high_score = 0
# score = 0
# apple_pos = randonize
# apple = pygame.Surface((10, 10))
# apple.fill((255, 0, 0))
# my_direction = LEFT


# pygame.display.set_caption(
#     'Snake - ' + str(score) + ' Pontos - Nível: ' + str(VEL-10))

# while True:
#     clock.tick(VEL)
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#         if event.type == KEYDOWN:
#             if event.key == K_UP:
#                 my_direction = UP
#             if event.key == K_DOWN:
#                 my_direction = DOWN
#             if event.key == K_LEFT:
#                 my_direction = LEFT
#             if event.key == K_RIGHT:
#                 my_direction = RIGHT
#             if event.key == K_q:
#                 pygame.quit()
#             if event.key == K_k:
#                 my_direction = END

#     if collision(snake[0], apple_pos):
#         for x in range(TAIL):
#             snake.append((0, 0))
#         if QUANT_FRUIT < 10:
#             TAIL = 1
#             apple.fill((255, 0, 0))
#             QUANT_FRUIT = QUANT_FRUIT + 1
#         else:
#             TAIL = 5
#             apple.fill((100, 100, 100))
#             QUANT_FRUIT = 0
#             VEL = VEL + 1
#         apple_pos = randonize
#         score = score + 10
#         pygame.display.set_caption(
#             'Snake - ' + str(score) + ' Pontos - Nível: ' + str(VEL-10))

#     for i in range(len(snake) - 1, 0, -1):
#         snake[i] = (snake[i-1][0], snake[i-1][1])

#     if my_direction == UP:
#         snake[0] = (snake[0][0], snake[0][1] - 10)
#     if my_direction == DOWN:
#         snake[0] = (snake[0][0], snake[0][1] + 10)
#     if my_direction == RIGHT:
#         snake[0] = (snake[0][0] + 10, snake[0][1])
#     if my_direction == LEFT:
#         snake[0] = (snake[0][0] - 10, snake[0][1])
#     if my_direction == END:
#         snake[0] = (snake[0][0], snake[0][1])

#     screen.fill((0, 0, 0))
#     screen.blit(apple, apple_pos)
#     for pos in snake:
#         screen.blit(snake_skin, pos)

#     pygame.display.update()
