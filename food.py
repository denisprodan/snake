import pygame
from random import randrange


class Food:
	def __init__(self,size):
		self.x = 0
		self.y = 0
		self.size = size

	def pickLocation(self, rows, tail):
		self.x = randrange(rows)
		self.y = randrange(rows)
		while [self.x, self.y] in tail:
			self.x = randrange(rows)
			self.y = randrange(rows)


	def draw(self, surface):
		pygame.draw.rect(surface, (231,23,230), (self.x*self.size, self.y*self.size,self.size, self.size))