from cardinals import cardinals
from random import randint
from random import choice
from random import shuffle
from tunneler import Tunneler
import pygame

class TunnelNode(object):


	def __init__(self, maze, builder = None):
	
		self.maze = maze
		self.builder = builder
		self.tunnelers = []
		
		
		if builder is None:
			self.position = maze.origin
		else:
			self.position = self.builder.position
		
		if self.maze.inRange(self.position):
			self.spawnTunnelers()		
		
	def spawnTunnelers(self):
	
		if self.builder is None:
			dir = choice(cardinals.values())
		else:
			dir = self.builder.direction
			
		entryDir = (dir[0] * -1, dir[1] * -1)
	
		dirs = cardinals.values()
				
		for dir in dirs:

			if dir == entryDir:
				continue
			
			if len(self.maze.nodes) == 0:
				self.tunnelers.append(Tunneler(self.maze, self.position, dir))
			elif randint(0, 1) == 0:
				self.tunnelers.append(Tunneler(self.maze, self.position, dir))
		
	def update(self):
	
		for tunneler in self.tunnelers:
			tunneler.update()
			
	def isDone(self):
			
		for tunneler in self.tunnelers:
			if not tunneler.isDone():
				return False
				
		return True
		
	def draw(self, surface, color = (255, 0, 0)):
	
		for tunneler in self.tunnelers:
			tunneler.draw(surface)
	
		pos = (self.position[0] - 5, self.position[1] - 5)
		rect = (pos, (10, 10))
		pygame.draw.rect(surface, color, rect)
		

		



		
		
	