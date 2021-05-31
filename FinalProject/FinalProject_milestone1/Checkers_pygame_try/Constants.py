import pygame

WIDTH, HEIGHT = 500, 500
COLS, ROWS = 8, 8
SQUARE_SIZE = WIDTH // COLS

RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)

WIN = pygame.display.set_mode((WIDTH,HEIGHT))

CROWN = pygame.transform.scale(pygame.image.load("Checkers_pygame_try\\crow.png"), (45, 25))