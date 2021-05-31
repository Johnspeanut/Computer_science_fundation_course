import pygame
from .Pieces import Pieces
from .Constants import WIDTH, HEIGHT, COLS, ROWS, SQUARE_SIZE, RED, WHITE,GREY, BLACK, WIN
from .piece import Piece

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
    
    def update(self,win):
        self.board.draw_pieces(win)
        pygame.display.update()
    
    def _init(self):
        self.selected = None
        self.board = Pieces()
        self.turn = RED
        self.valid_moves = {}

    def reset(self):
        self._init()
    
    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        else:
            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True
        return False
    
    def _move(self, row, col):
        

