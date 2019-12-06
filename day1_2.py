import day1_1

"""
Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2. However, that fuel also requires fuel, and that fuel requires fuel, and so on. Any mass that would require negative fuel should instead be treated as if it requires zero fuel; the remaining mass, if any, is instead handled by wishing really hard, which has no mass and is outside the scope of this calculation.
"""

def _fuel_required(mass):
	fuel = day1_1.fuel_required(mass)
	if fuel < 0:
		fuel = 0
	return fuel

def fuel_required(mass):
	fuel = x = _fuel_required(mass)
	while (True):
		x = _fuel_required(x)
		fuel += x
		if x == 0:
			break

	return fuel

"""
A module of mass 14 requires 2 fuel. This fuel requires no further fuel (2 divided by 3 and rounded down is 0, which would call for a negative fuel), so the total fuel required is still just 2.

At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires 216 more fuel (654 / 3 - 2). 216 then requires 70 more fuel, which requires 21 fuel, which requires 5 fuel, which requires no further fuel. So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.

The fuel required by a module of mass 100756 and its fuel is: 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.
"""
if __name__ == '__main__':
	assert(fuel_required(mass=12) == 2)
	assert(fuel_required(mass=14) == 2)
	assert(fuel_required(mass=1969) == 966)
	assert(fuel_required(mass=100756) == 50346)
	print 'Day 1 part 2 tests passed'
	
	total = 0
	for i in day1_1.inputs:
		total += fuel_required(i)
	print total