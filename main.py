import pygame
from snake import Snake
from food import Food
import tkinter
from tkinter import messagebox
def message(score):
	root = tkinter.Tk()
	root.withdraw()
	messagebox.showinfo(title='You lost', message = 'Your score is '+ str(score))
width = 500
height = 500
rows = 20
size_row = width // rows
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake game")
s = Snake()
f = Food(size_row)
def update_scr(win):
	global s, size_row,f,rows
	win.fill((127,127,127))
	s.draw(win, size_row)
	f.draw(win)
	pygame.display.update()
clock = pygame.time.Clock()
f.pickLocation(rows, s.tail)
while True:
	pygame.time.delay(80)
	clock.tick(100)
	if s.eatFood(f):
		f.pickLocation(rows, s.tail)
	if s.death():
		message(s.total)
		s.stop()
	s.update(rows)
	update_scr(win)
