
from cardinals import Cardinal

class Coord:

	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def add(self, dir, amount):
		
		if dir is Cardinal.NORTH:
			self.y -= amount
		if dir is Cardinal.SOUTH:
			self.y += amount
		if dir is Cardinal.WEST:
			self.x -= amount
		if dir is Cardinal.EAST:
			self.x += amount
	
	def copy(self):
		return Coord(self.x, self.y)