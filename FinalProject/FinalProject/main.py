"""
Student name:Qiong Peng; NUID: 001559637
CS5001 Section 4, Fall 2020
Final project
The project is to design a checkers game using the Turtle module and built-in
functions of Python.
I create a few classes and the main.py is the start. The current version of the
game can function fully. When a piece reaches the opposite baseline,
the outline of the piece changes yellow, whitch indicates it become a king.
At the end of the game, the name of winner will prompt on the screen. The files
have been pushed to github repos and the folder name is "Qiong_Peng_repository/
FinalProject/FinalProject"
"""

import turtle
from constant import ROWS, COLS, SQUARE_SIZE
from gamestate import GameState
from piece import Piece
from board import Board


def main():
    board_size = COLS * SQUARE_SIZE
    window_size = board_size + SQUARE_SIZE
    turtle.setup(window_size, window_size)
    turtle.screensize(board_size, board_size)
    turtle.bgcolor("white")
    turtle.tracer(0, 0)
    screen = turtle.Screen()
    screen.title("Checkers")
    game = GameState()
    board = Board()
    board.draw_chess_quares()
    game.draw_pieces()
    screen.onclick(game.update)
    screen.listen()
    turtle.done()


if __name__ == "__main__":
    main()
