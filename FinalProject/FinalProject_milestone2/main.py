""" 
Student name:Qiong Peng; NUID: 001559637
CS5001 Section 4, Fall 2020
Final project
The project is to design a checkers game using the Turtle module and built-in
functions of Python.
I create a few classes and the main.py is the start. main.py is a higher level
than other files. That's why the import file dictionary in the main.py is
different from other else. The current version of the game can function fully.
When a piece reaches the opposite baseline, the outline of the piece changes
yellow, whitch indicates it become a king. At the end of the game, the name of
winner will prompt.
The files were pushed to github and the folder name is "Qiong_Peng_repository/
FinalProject/FinalProject_milestone2"
"""

import turtle
from MileStone2.constant import ROWS, COLS, SQUARE_SIZE
from MileStone2.gamestate import GameState
from MileStone2.piece import Piece
from MileStone2.board import Board


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
