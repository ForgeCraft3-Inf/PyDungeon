#!/usr/bin/python

import pygame
from maze import Maze

from pygame.locals import *
from coord import Coord

pygame.init()

class Main(object):


	def __init__(self):
		size = 500
		self.surface = pygame.display.set_mode((size, size))
		mazeOrigin = Coord(size/2, size/2)
		self.maze = Maze(mazeOrigin.copy())

		done = False
		
		while(not done):
			self.surface.fill((255,255,255))
			self.maze.update()
			self.maze.draw(self.surface)
			pygame.display.flip()
			
			event = pygame.event.get()
		 
			for e in event:
				if(e.type == QUIT):
					done = True
		 
				elif(e.type == KEYDOWN):
		 
					if(e.key == K_q):
						done = True
				   
					if(e.key == K_r):
						self.maze = Maze(Coord(size/2, size/2))
			
			
			
Main()