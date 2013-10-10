from cardinals import cardinals
from random import randint
import pygame

class Tunneler(object):

	def __init__(self, maze, origin, direction):
		
		self.maze = maze
		
		self.tunnel = []
		
		self.direction = direction
		self.position = origin
		self.done = False
		self.extend = 20
		
	def update(self):
	
		if self.maze.full():
			return

		if self.done:
			return
	
		if(self.maze.hasNearbyNode(self.position)):
			self.advance()
		else:
			if randint(0, self.extend) == 0:	
				self.maze.spawnNode(self)
				self.done = True
			else:
				self.advance()
				self.extend -= 1
			
		self.tunnel.append(self.position)
	
	def advance(self):	
		newX = self.position[0] + self.direction[0]
		newY = self.position[1] + self.direction[1]
		self.position = (newX, newY)

	def isDone(self):
		
		if self.maze.full():
			return True
		
		return self.done
		
	def draw(self, surface):
	
		for point in self.tunnel:
			pos = (point[0] - 1, point[1] - 1)
			rect = (pos, (3, 3))
			pygame.draw.rect(surface, (0, 0, 0), rect)

		
		