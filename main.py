import pygame
from pygame.locals import *
from func import tic_tac, draw_board, check_is_game_over
from const import screen_width, screen_height, bg_color, line_color

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
is_game_over = False
player = 1
clicked = False


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Крестики-Нолики')

run = True
while run:
    draw_board(screen, bg_color, line_color)
    tic_tac(board, screen)
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if not is_game_over:
            if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0] // 100
                cell_y = pos[1] // 100
                if board[cell_x][cell_y] == 0:
                    board[cell_x][cell_y] = player
                    player *= -1
                    check_is_game_over(board)
    pygame.display.update()
