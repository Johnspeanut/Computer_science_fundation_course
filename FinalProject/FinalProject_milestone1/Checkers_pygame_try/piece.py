import pygame
from .Constants import WIDTH, HEIGHT, COLS, ROWS, SQUARE_SIZE, RED, WHITE,GREY, BLACK, CROWN

PADDING = 10
OUTLINE = 2


class Piece:
    def __init__(self, row, col, color):
        self.col = col
        self.row = row
        self.color = color
        self.isKing = False
        self.center_x, self.center_y  = 0,0
        self.center_x, self.center_y  = self.calc_center_x_y()
        self.direction = 0
        self.move_direction()
    
    def getColor(self):
        return self.color
    
    def getCol(self):
        return self.col


    def calc_center_x_y(self):
        center_x = self.col * SQUARE_SIZE + SQUARE_SIZE / 2
        center_y = self.row * SQUARE_SIZE+ SQUARE_SIZE / 2
        return center_x, center_y
    
    def draw_piece(self, win):
        radius = SQUARE_SIZE / 2 - PADDING
        pygame.draw.circle(win, self.color, (self.center_x, self.center_y), radius + OUTLINE)
        pygame.draw.circle(win, self.color, (self.center_x, self.center_y), radius)
        if self.isKing:
            win.blit(CROWN, (self.center_x - CROWN.get_width()//2, self.center_y - CROWN.get_height()//2))
    
    def move_piece(self, des_row, des_col):
        self.col = des_col
        self.row = des_row
        self.calc_center_x_y()
    
    def make_king(self):
        self.isKing = True
    
    def move_direction(self):
        if self.isKing:
            self.direction = 0
        elif self.color == RED and self.isKing == False:
            self.direction = 1 
        else:
            self.direction = 2

    def __repr_(self):
        return str(self.color)
        
    


        


