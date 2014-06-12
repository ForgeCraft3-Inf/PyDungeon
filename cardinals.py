
class Cardinal:

	NORTH = 1
	SOUTH = 2
	EAST = 3
	WEST = 4
	
	DIRECTIONS = [NORTH, SOUTH, EAST, WEST]
	
	@staticmethod
	def reverse(dir):
		if dir is Cardinal.NORTH: return Cardinal.SOUTH
		if dir is Cardinal.SOUTH: return Cardinal.NORTH
		if dir is Cardinal.EAST: return Cardinal.WEST
		if dir is Cardinal.WEST: return Cardinal.EAST