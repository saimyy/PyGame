import pygame
from pygame.locals import *


def draw_board():
    screen.fill(bg_color)
    for i in range(1, 3):
        pygame.draw.line(screen, grid, (0, i * 200), (600, i * 200), 8)
        pygame.draw.line(screen, grid, (i * 200, 0), (i * 200, 600), 8)


screen_width = 600
screen_height = 600
bg_color = (245, 234, 203)
grid = (50, 50, 50)

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