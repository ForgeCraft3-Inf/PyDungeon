from cardinals import Cardinal
from random import randint
import pygame

class Tunneler(object):

	MIN_LENGTH = 20

	def __init__(self, maze, origin, direction):

		
	
		self.maze = maze
		
		self.tunnel = []
		
		self.direction = direction
		self.position = origin.copy()
		self.done = False

		
	def update(self):
	
		if self.maze.full():
			return

		if self.done:
			return
	
		if(self.maze.hasNearbyNode(self.position)):
			self.advance()
		else:
			if len(self.tunnel) > Tunneler.MIN_LENGTH and randint(0, 5) == 0:
				self.maze.spawnNode(self)
				self.done = True
			else:
				self.advance()
			
		self.tunnel.append(self.position.copy())
	
	def advance(self):	
		self.position.add(self.direction, 1)

	def isDone(self):
		
		if self.maze.full():
			return True
		
		return self.done
		
	def draw(self, surface):
	
		for point in self.tunnel:
			pos = (point.x - 1, point.y - 1)
			rect = (pos, (3, 3))
			pygame.draw.rect(surface, (0, 0, 0), rect)

		
		