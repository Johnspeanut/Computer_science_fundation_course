import pygame
from Checkers_pygame_try.Pieces import Pieces
from Checkers_pygame_try.Constants import WIDTH, HEIGHT, COLS, ROWS, SQUARE_SIZE, RED, WHITE,GREY, BLACK, WIN
from Checkers_pygame_try.Game import Game


FPS = 60
pygame.display.set_caption("Checkers game")

def get_col_row_from_mouse(pos):
    x, y = pos
    col = x // SQUARE_SIZE
    row = y // SQUARE_SIZE
    return row, col

def main():
    clock = pygame.time.Clock()
    clock.tick(FPS)
    game = Game(WIN)
    # one_piece = pieces.get_piece(1, 0)
    # pieces.move_one_piece_on_board(3, 0, one_piece)
    # one_piece = pieces.get_piece(1, 0)
    # print(one_piece.col, one_piece.row)
    # pieces.move_pieces(3, 4, one_piece)
    # pieces.draw_pieces(WIN)
    # pygame.display.update()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_col_row_from_mouse(pos)
                # piece = pieces.get_piece(row, col)
                # pieces.move_one_piece_on_board(4, 3, piece)
        game.update(WIN)
        # pieces.draw_pieces(WIN)
        # pygame.display.update()
    pygame.quit()
    # pygame.display.update()
        


main()