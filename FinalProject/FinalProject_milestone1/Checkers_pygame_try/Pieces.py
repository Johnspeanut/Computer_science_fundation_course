import pygame
from .piece import Piece
from .Constants import WIDTH, HEIGHT, COLS, ROWS, SQUARE_SIZE, RED, WHITE,GREY, BLACK, WIN


class Pieces:
    def __init__(self):
        self.pieces = []
        # self.create_pieces(pieces)
        # self.draw_pieces(win, pieces)
        # self.draw_squares(win)
        # self.selected_piece = None
        self.red_left = self.white_left = 12
        self.create_pieces()
        self.white_kings, self.red_kings = 0, 0
        # self.draw_pieces(win)
        # self.draw_squares(win)


    
    def create_pieces(self):
        for i in range(ROWS):
            self.pieces.append([])
            for j in range(COLS):
                if (i + j) % 2 == 0:
                    self.pieces[i].append(0)
                elif i < 3:
                    self.pieces[i].append(Piece(i, j, WHITE))
                elif i > 4:
                    self.pieces[i].append(Piece(i, j, RED))
                else:
                    self.pieces[i].append(0)


    def draw_pieces(self, win):
        self.draw_squares(win)
        for i in range(ROWS):
            for j in range(COLS):
                piece = self.pieces[i][j]
                if piece != 0:
                    piece.draw_piece(win)

    
    def draw_squares(self, win):
        for i in range(ROWS):
            for j in range(COLS):
                if (i + j) % 2 == 0:
                    pygame.draw.rect(win, WHITE, (i*SQUARE_SIZE, j*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                else:
                    pygame.draw.rect(win, GREY, (i*SQUARE_SIZE, j*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    def move_one_piece_on_board(self, to_row, to_col, piece):
        self.pieces[piece.row][piece.col], self.pieces[to_row][to_col] = self.pieces[to_row][to_col], self.pieces[piece.row][piece.col]
        piece.move_piece(to_row, to_col)
        if to_row == ROWS - 1 or to_row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1
    
    def get_piece(self, row, col):
        return self.pieces[row][col]





