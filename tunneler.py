from cardinals import Cardinal
from random import randint
import pygame

class Tunneler(object):

	MIN_LENGTH = 20

	def __init__(self, maze, node, direction):

		
		self.parent = node
		self.maze = maze
		self.tunnel = []
		self.direction = direction
		self.position = node.position.copy()
		self.done = False
		self.end = None

		
	def update(self):
	
		if self.maze.full():
			if self.end is None:
				self.parent.remove(self)
			return

		if self.done:
			return
	
		if(self.maze.hasNearbyNode(self.position)):
			self.advance()
		else:
			if len(self.tunnel) > Tunneler.MIN_LENGTH and randint(0, 5) == 0:
				self.end = self.maze.spawnNode(self)
				self.done = True
			else:
				self.advance()
		
		for node in self.maze:
			if self.done: break
		
			if node is self.parent: continue
		
			if node.overlap(self.position, 3):
				self.parent.remove(self)
			
		self.tunnel.append(self.position.copy())
	
	def advance(self):
		self.position.add(self.direction, 1)
		if self.maze.hasIntersect(self):
			self.parent.remove(self)
			
		

	def isDone(self):
		
		if self.maze.full():
			return True
		
		return self.done
		
	def draw(self, surface):
	
		for point in self.tunnel:
			pos = (point.x - 1, point.y - 1)
			rect = (pos, (3, 3))
			pygame.draw.rect(surface, (0, 0, 0), rect)

	def intersect(self, tunneler):
	
		if tunneler is self: return False
		
		if tunneler.parent is self.end: return False
		
		if tunneler.parent is self.parent: return False
	
		if not Cardinal.isOrthogonal(self.direction, tunneler.direction): return False
		
		if self.direction in [Cardinal.NORTH, Cardinal.SOUTH]:
		
			if self.direction == Cardinal.NORTH:
				north = self.position.y
				south = self.parent.position.y
			else:
				south = self.position.y
				north = self.parent.position.y
			
			if tunneler.position.y > south: return False
			if tunneler.position.y < north: return False
			
			if tunneler.position.x != self.position.x: return False
			
		if self.direction in [Cardinal.EAST, Cardinal.WEST]:
		
			if self.direction == Cardinal.EAST:
				east = self.position.x
				west = self.parent.position.x
			else:
				west = self.position.x
				east = self.parent.position.x
				
			if tunneler.position.x < west: return False
			if tunneler.position.x > east: return False
			
			if tunneler.position.y != self.position.y: return False
			
		return True
		
			
	def __iter__(self):
		return iter(self.tunnel)
		