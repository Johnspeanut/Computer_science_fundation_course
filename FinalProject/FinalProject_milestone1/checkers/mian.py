import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED
from checkers.board import Board
from checkers.game import Game
# from minimax.algorithm import minimax

FPS = 60
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Checkers game")

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    clock = pygame.time.Clock()
    game = Game(WIN)
    run = True
    while run:
        clock.tick(FPS)
        if game.winner() != None:
            print(game.winer())
            run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col, row = get_row_col_from_mouse(pos)
                game.select(col, row)
        game.update()
    pygame.quit()


main()
