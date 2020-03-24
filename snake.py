import pygame
import sys


class Snake:
	tail = []
	def __init__(self):
		self.x = 0
		self.y = 0
		self.xS = 1
		self.yS = 0
		self.total = 0
	def draw(self, surface, size):
		for i in range(len(self.tail)):
			pygame.draw.rect(surface, (230,230,230), (self.tail[i][0]*size,self.tail[i][1]*size,size,size))
		pygame.draw.rect(surface, (230,230,230), (self.x*size, self.y*size,size, size))
		pygame.draw.circle(surface, (0,0,0), (self.x*size + size//4,self.y*size + size//4),1)
		pygame.draw.circle(surface, (0,0,0), (self.x*size + 3*size//4,self.y*size + size//4),1)
	def eatFood(self, food):
		if self.x == food.x and self.y == food.y:
			self.total += 1
			return True
		else:
			return False
	def update(self):
		if self.total == len(self.tail):
			for i in range(0,len(self.tail)-1):
				self.tail[i] = self.tail[i+1]
				self.tail[-1] = [self.x, self.y]
			if self.total == 1:
				self.tail[0] = [self.x, self.y]
		else:
			self.tail.append([self.x, self.y])
			for i in range(0,len(self.tail)-1):
				self.tail[i] = self.tail[i+1]
				self.tail[-1] = [self.x, self.y]


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					self.yS = 1
					self.xS = 0
				if event.key == pygame.K_UP:
					self.yS = -1
					self.xS = 0
				if event.key == pygame.K_RIGHT:
					self.yS = 0
					self.xS = 1
				if event.key == pygame.K_LEFT:
					self.yS = 0
					self.xS = -1
		self.x += self.xS
		self.y += self.yS