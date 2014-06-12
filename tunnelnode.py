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
				
		toSkip = choice(Cardinal.DIRECTIONS)
				
		for dir in Cardinal.DIRECTIONS:

			if dir == entryDir:
				continue
				
			if dir == toSkip:
				continue
			
			self.tunnelers.append(Tunneler(self.maze, self, dir))
		
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
		

	def overlap(self, pos, buffer=0):
		
		if not abs(pos.x - self.position.x) + buffer < self.size / 2: return False
		if not abs(pos.y - self.position.y) + buffer < self.size / 2: return False
		return True

	def nodeOverlap(self, node, buffer=0):
		
		distX = abs(node.position.x - self.position.x)
		minDist = self.size/2 + node.size/2 + buffer
		if not (distX < minDist): return False
		
		distY = abs(node.position.y - self.position.y)
		if not (distY < minDist): return False
		
		return True
		
	def remove(self, tunneler):
		if tunneler in self.tunnelers:
			self.tunnelers.remove(tunneler)

	def __iter__(self):
		return iter(self.tunnelers)
		
	