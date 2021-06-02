import pygame
from .constants import RED, WHITE, GREY, SQUARE_SIZE, CROWN

class Piece:		# piece class stores information about the piece( king, xy postion, allow user to move piece)
	PADDING = 12.5
	OUTLINE = 2		# outline of piece

	def __init__(self, row, col, color):
		self.row = row
		self.col = col
		self.color = color
		self.king = False

		self.x = 0
		self.y = 0
		self.calc_pos()

	def calc_pos(self):		# cacl x and y postion based on row/column located in. Square size must be known so that i can mutliple whatever row/col is selected so starting  xy pos is known when piece is drawn
		self.x = SQUARE_SIZE*self.col + SQUARE_SIZE // 2		# piece is placed in middle of square when x and y postitions are defined. pieces are circular therefore divided radius by 2 so is in the middle of square
		self.y = SQUARE_SIZE*self.row + SQUARE_SIZE // 2

	def make_king(self):		# changes to king
		self.king = True

	def draw(self, win):		# draw piece
		radius = SQUARE_SIZE//2 - self.PADDING
		pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
		pygame.draw.circle(win, self.color, (self.x, self.y), radius)
		if self.king:
			win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))		# draw crown in the middle

	def move(self, row, col):		# move piece. here deletion of piece from where currently is placed occurs and postion is change
		self.row = row
		self.col = col
		self.calc_pos()

	def __repr__(self):
		return str(self.color)