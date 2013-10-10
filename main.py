#!/usr/bin/python

import pygame
from maze import Maze

from pygame.locals import *

pygame.init()

class Main(object):


	def __init__(self):
		size = (500, 500)
		self.surface = pygame.display.set_mode(size)
		mazeOrigin = (250, 250)		
		self.maze = Maze(mazeOrigin)

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
						self.maze = Maze(mazeOrigin)
			
			
			
Main()