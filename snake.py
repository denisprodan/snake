import pygame
import sys

class Snake:
	tail = []
	t = True
	b = True
	r = True
	l = True
	def __init__(self):
		pygame.init()
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

	def death(self):
		if [self.x, self.y] in self.tail:
			return True
		else:
			return False

	def stop(self):
		flag = True
		while flag:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					flag = False
					self.reset()
	def reset(self):
		self.tail = []
		self.x = 0
		self.y = 0 
		self.xS = 1
		self.yS = 0
		self.total = 0

	def update(self, rows):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN and self.b:
					self.yS = 1
					self.xS = 0
					self.t = False
					self.r = True 
					self.l = True
				if event.key == pygame.K_UP and self.t:
					self.yS = -1
					self.xS = 0
					self.b = False
					self.r = True 
					self.l = True
				if event.key == pygame.K_RIGHT and self.r:
					self.yS = 0
					self.xS = 1
					self.l = False
					self.t = True
					self.b = True
				if event.key == pygame.K_LEFT and self.l:
					self.yS = 0
					self.xS = -1
					self.r = False
					self.t = True
					self.b = True
		if self.x > rows - 1:
			self.x = 0
		elif self.x < 0:
			self.x = rows - 1
		elif self.y > rows - 1:
			self.y = 0
		elif self.y < 0:
			self.y = rows - 1
		if self.total == len(self.tail):
			if len(self.tail) > 0:
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
		self.x += self.xS
		self.y += self.yS
