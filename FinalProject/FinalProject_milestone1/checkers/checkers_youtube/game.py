import pygame
from .board import Board 
from .constants import RED, WHITE, BLUE, SQUARE_SIZE


class Game:
    def __init__(self, win):
        self._init()
        self.win = win


    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()


    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}


    def reset(self):
        self._init()


    def winner(self):
        return self.board.winner()


    def select(self,col, row):
        if self.selected != None:
            result = self._move(col, row)
            if not result:
                self.selectd = None
                self.select(col, row)
        piece = self.board.get_piece(col, row)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        return False


    def _move(self, col, row):
        piece = self.board.get_piece(col, row)
        if self.selected and piece == 0 and (col, row) in self.valid_moves:
            self.board.move(self.selected, col, row)
            skipped = self.valid_moves[(col, row)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        return True


    def draw_valid_moves(self, moves):
        for move in moves:
            col, row = move
            pygame.draw.circle(self.win, BLUE, (col*SQUARE_SIZE + SQUARE_SIZE//2, row*SQUARE_SIZE + SQUARE_SIZE//2), 15)


    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED






