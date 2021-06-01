
import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from minimax.algorithm import minimax

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers - AI mode')

def get_row_col_from_mouse(pos):        #  method which uses the position of the mouse and output, based on the postion of the mouse what row and column currently in
    x, y = pos      #  xy will be equal to pos as pos will be a tuple which will have the x and y positions of the mouse, based on the square size i can know what row/col currently in
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():     #  event loop in main function will run every x times per sec, func check to see if user has pressed on something, then update accordingly
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 3, WHITE, game)
            game.ai_move(new_board)

        if game.winner() != None:       # check winner
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    
    pygame.quit()

main()