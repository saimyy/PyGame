import pygame
from pygame.locals import *
from const import screen_width, screen_height, bg_color, line_color


def draw_board():
    screen.fill(bg_color)
    for i in range(1, 3):
        pygame.draw.line(screen, line_color, (0, i * 100), (300, i * 100), 6)
        pygame.draw.line(screen, line_color, (i * 100, 0), (i * 100, 300), 6)


def check_is_game_over():
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


def tic_tac():
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


board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
is_game_over = False
players_turn = 1
is_clicked = False
winner = 0
position = (0, 0)

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Крестики-Нолики')
font = pygame.font.SysFont('arial', 30)
again_rect = Rect(screen_width // 2 - 80, screen_height // 2, 166, 50)


def draw_game_over(win):
    end_text = f'Игрок {win} победил!' if winner != 0 else 'Вы сыграли вничью!'
    pygame.draw.rect(screen, (0, 255, 0), (300 // 2 - 100, 300 // 2 - 60, 200, 50))
    screen.blit(font.render(end_text, True, (0, 0, 255)), (300 // 2 - 100, 300 // 2 - 50))
    pygame.draw.rect(screen, (0, 255, 0), again_rect)
    screen.blit(font.render('Играть снова?', True, (0, 0, 255)), (300 // 2 - 80, 300 // 2 + 10))


run = True
while run:
    draw_board()
    tic_tac()
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if not is_game_over:
            if event.type == pygame.MOUSEBUTTONDOWN and not is_clicked:
                is_clicked = True
            if event.type == pygame.MOUSEBUTTONUP and is_clicked:
                is_clicked = False
                position = pygame.mouse.get_pos()
                cell_x = position[0] // 100
                cell_y = position[1] // 100
                if board[cell_x][cell_y] == 0:
                    board[cell_x][cell_y] = players_turn
                    players_turn *= -1
                    check_is_game_over()
    if is_game_over:
        draw_game_over(winner)
        if event.type == pygame.MOUSEBUTTONDOWN and not is_clicked:
            is_clicked = True
        if event.type == pygame.MOUSEBUTTONUP and is_clicked:
            is_clicked = False
            position = pygame.mouse.get_pos()
            if again_rect.collidepoint(position):
                is_game_over = False
                players_turn = 1
                position = (0, 0)
                board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                winner = 0
    pygame.display.update()
pygame.quit()
