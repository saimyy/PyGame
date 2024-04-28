import pygame
from pygame.locals import *

is_game_over = False
player = 1
clicked = False


def draw_board(screen, bg_color, line_color):
    screen.fill(bg_color)
    for i in range(1, 3):
        pygame.draw.line(screen, line_color, (0, i * 100), (300, i * 100), 6)
        pygame.draw.line(screen, line_color, (i * 100, 0), (i * 100, 300), 6)


def tic_tac(board, screen):
    i = 0
    for i, x in enumerate(board):
        j = 0
        for j, y in enumerate(x):
            if y == 1:
                pygame.draw.line(screen, (255, 123, 0), (i * 100 + 15, j * 100 + 15),
                                 (i * 100 + 85, j * 100 + 85), 6)
                pygame.draw.line(screen, (255, 123, 0), (i * 100 + 85, j * 100 + 15),
                                 (i * 100 + 15, j * 100 + 85), 6)
            if y == -1:
                pygame.draw.circle(screen, (0, 251, 255), (i * 100 + 50, j * 100 + 50), 38, 6)
        i += 1


def check_is_game_over(board):
    global is_game_over
    global winner
    for j, x in enumerate(board):
        if sum(x) == 3:
            winner = 1
            is_game_over = True
        if sum(x) == -3:
            winner = 2
            is_game_over = True
        if board[0][j] + board[1][j] + board[2][j] == 3:
            winner = 1
            is_game_over = True
        if board[0][j] + board[1][j] + board[2][j] == -3:
            winner = 2
            is_game_over = True
    if board[0][0] + board[1][1] + board[2][2] == 3 or board[2][0] + board[1][1] + board[0][2] == 3:
        winner = 1
        is_game_over = True
    if board[0][0] + board[1][1] + board[2][2] == -3 or board[2][0] + board[1][1] + board[0][2] == -3:
        winner = 2
        is_game_over = True

    if not is_game_over:
        is_tie = True
        for row in board:
            for i in row:
                if i == 0:
                    is_tie = False
        if is_tie:
            is_game_over = True
            winner = 0
