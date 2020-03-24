import pygame
from snake import Snake
from food import Food

width = 500
height = 500
rows = 20
size_row = width // rows
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake game")
s = Snake()
f = Food(size_row)
def update_scr(win):
	global s, size_row,f
	win.fill((127,127,127))
	s.draw(win, size_row)
	f.draw(win)
	pygame.display.update()
clock = pygame.time.Clock()
f.pickLocation(rows)
while True:
	pygame.time.delay(50)
	clock.tick(15)
	if s.eatFood(f):
		f.pickLocation(rows)
	s.update()
	update_scr(win)