from day3_1 import inputs, manhattan_distance

# Return list of coordinates for each point in the wire grid.
# The tuple returned is (x, y, total_steps) where total steps is the length of the wire up to that point.
def wire_path_coords(wire_path):
	wire_path = wire_path.split(",")
	coords = []
	for step in wire_path:
		direction = step[0]
		steps = int(step[1:])
		if len(coords) == 0:
			current_point = (0,0,0)
		else:
			current_point = coords[-1]
		for i in range(1, steps + 1):
			if direction == 'R':
				coords.append((current_point[0] + i, current_point[1], current_point[2] + i))
			if direction == 'L':
				coords.append((current_point[0] - i, current_point[1], current_point[2] + i))
			if direction == 'U':
				coords.append((current_point[0], current_point[1] + i, current_point[2] + i))
			if direction == 'D':
				coords.append((current_point[0], current_point[1] - i, current_point[2] + i))
	return coords

def find_closest_wire_intersection_by_length(wire_path1, wire_path2):
	coords1 = wire_path_coords(wire_path1)
	coords2 = wire_path_coords(wire_path2)

	coords1_dict = {}
	coords2_dict = {}
	for x,y,z in coords1:
		coords1_dict["%s,%s" % (x, y)] = (x,y,z)
	for x,y,z in coords2:
		coords2_dict["%s,%s" % (x, y)] = (x,y,z)
	intersections = [[coords1, coords2_dict[key]] for key,coords1 in coords1_dict.iteritems() if key in coords2_dict]
	
	# print [manhattan_distance(coords[0], coords[1]) for coords in intersections]
	shortest = sorted(intersections, cmp=lambda a,b: (a[0][2] + a[1][2]) - (b[0][2] + b[1][2]))[0]
	return shortest[0][2] + shortest[1][2]

def sorted_wire_distance_cmp(a, b):
	return (a[0][2] + a[1][2]) - (b[0][2] + b[1][2])

"""
Here are the best steps for the extra examples from above:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps
"""
if __name__ == '__main__':
	assert find_closest_wire_intersection_by_length('R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83') == 610
	assert find_closest_wire_intersection_by_length('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7') == 410
	
	print 'Day 3 part 2 tests passed'
	print 
	print find_closest_wire_intersection_by_length(inputs[0], inputs[1])
	
	