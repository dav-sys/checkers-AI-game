import pygame

# consists of constant variables
# any variable changes can be implemented here if needed
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS
# size of one square in checkers board
# RGB
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)


CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))