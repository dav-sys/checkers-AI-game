import pygame
from .constants import RED, WHITE, BLUE, SQUARE_SIZE
from checkers.board import Board

class Game:     # game class allows user to interface with board/pieces.
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

    def winner(self):
        return self.board.winner()

    def reset(self):    # rest method to rest
        self._init()

    def select(self, row, col):     # if selected something, will move what i have selected to row/column
        if self.selected:
            result = self._move(row, col)
            if not result:      # if selected row/col is valid move will occur, if not will be able to try and select a different piece
                self.selected = None
                self.select(row, col)       # call method again
        
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
            
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)        # move selected piece to row and column
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):      # checks all of the diagonals of where the  piece is, draw squares for all of these valid moves
        for move in moves:      # loops through all the keys of the dictionary ( row/col identified as a tuple)
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self):      # change turn of players
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()