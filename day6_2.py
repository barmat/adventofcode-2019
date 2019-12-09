from day6_1 import orbit_input, parse_orbits, _count_orbits

def orbit_list(obj, orbits):
	current_obj = obj
	orbit_data = []
	while (True):
		if current_obj == 'COM':
			break
		current_obj = orbits[current_obj]
		orbit_data.append(current_obj)
	return orbit_data
	

if __name__ == '__main__':
	mapped_data, objects = parse_orbits(orbit_input)
	you_orbits = orbit_list('YOU', mapped_data)
	san_orbits = orbit_list('SAN', mapped_data)
	
	you_count = 0
	for obj in you_orbits:
		try:
			san_count = san_orbits.index(obj)
			print you_count + san_count
			quit()
		except ValueError as e:
			pass
		you_count += 1
