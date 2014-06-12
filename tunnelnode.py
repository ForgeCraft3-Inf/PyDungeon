from cardinals import Cardinal
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
		self.size = 6 + randint(0, 20)
		
		
		if builder is None:
			self.position = maze.origin.copy()
		else:
			self.position = self.builder.position.copy()
		
		if self.maze.inRange(self.position):
			self.spawnTunnelers()		
		
	def spawnTunnelers(self):
	
		if self.builder is None:
			dir = choice(Cardinal.DIRECTIONS)
		else:
			dir = self.builder.direction
			
		entryDir = Cardinal.reverse(dir)
				
		for dir in Cardinal.DIRECTIONS:

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
	
		pos = (self.position.x - self.size/2, self.position.y - self.size/2)
		rect = (pos, (self.size, self.size))
		pygame.draw.rect(surface, color, rect)
		

		



		
		
	