import pygame
from pygame.locals import *


def draw_board():
    screen.fill(bg_color)
    for i in range(1, 3):
        pygame.draw.line(screen, line_color, (0, i * 200), (600, i * 200), 8)
        pygame.draw.line(screen, line_color, (i * 200, 0), (i * 200, 600), 8)


def tic_tac():
    i = 0
    for i, x in enumerate(board):
        j = 0
        for j, y in enumerate(x):
            if y == 1:
                pygame.draw.line(screen, (255, 123, 0), (i * 200 + 15, j * 200 + 15),
                                 (i * 200 + 85, j * 200 + 85), 8)
                pygame.draw.line(screen, (255, 123, 0), (i * 200 + 85, j * 200 + 15),
                                 (i * 200 + 15, j * 200 + 85), 8)
            if y == -1:
                pygame.draw.circle(screen, (0, 251, 255), (i * 100 + 50, j * 100 + 50), 38, 8)
        i += 1


board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

screen_width = 600
screen_height = 600
bg_color = (245, 234, 203)
line_color = (50, 50, 50)

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Крестики-Нолики')

run = True
while run:
    draw_board()
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
    pygame.display.update()
