"""
Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.
"""
def fuel_required(mass):
	fuel = round(mass / 3) - 2
	return int(fuel)

inputs = [
	143754,
	83242,
	124730,
	62796,
	128187,
	68925,
	60687,
	68800,
	112450,
	70696,
	94653,
	62124,
	82251,
	91514,
	79895,
	82973,
	71678,
	141671,
	88243,
	109553,
	135097,
	78026,
	100048,
	52113,
	109934,
	92274,
	62821,
	138384,
	90112,
	114684,
	137383,
	71727,
	143236,
	79842,
	101187,
	71202,
	131156,
	128805,
	105102,
	71319,
	88615,
	62024,
	126027,
	55321,
	91226,
	75020,
	136689,
	70265,
	97850,
	96536,
	135311,
	64962,
	87137,
	50402,
	70604,
	56879,
	60016,
	98231,
	136635,
	64590,
	143522,
	112152,
	142511,
	95350,
	83483,
	123681,
	123792,
	99044,
	139282,
	96610,
	116844,
	50416,
	110682,
	55137,
	69795,
	100411,
	110119,
	141558,
	90780,
	108063,
	102247,
	85487,
	107174,
	79009,
	131908,
	95164,
	120588,
	62031,
	51070,
	63773,
	128565,
	96458,
	91388,
	54345,
	52840,
	130519,
	51357,
	146851,
	68455,
	102463,
]

"""
For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.
"""
if __name__ == '__main__':
	assert(fuel_required(mass=12) == 2)
	assert(fuel_required(mass=14) == 2)
	assert(fuel_required(mass=1969) == 654)
	assert(fuel_required(mass=100756) == 33583)
	print 'Day 1 part 2 tests passed'
	
	total = 0
	for i in inputs:
		total += fuel_required(i)
	print total