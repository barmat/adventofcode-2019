
inputs = """1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,6,19,23,1,10,23,27,2,27,13,31,1,31,6,35,2,6,35,39,1,39,5,43,1,6,43,47,2,6,47,51,1,51,5,55,2,55,9,59,1,6,59,63,1,9,63,67,1,67,10,71,2,9,71,75,1,6,75,79,1,5,79,83,2,83,10,87,1,87,5,91,1,91,9,95,1,6,95,99,2,99,10,103,1,103,5,107,2,107,6,111,1,111,5,115,1,9,115,119,2,119,10,123,1,6,123,127,2,13,127,131,1,131,6,135,1,135,10,139,1,13,139,143,1,143,13,147,1,5,147,151,1,151,2,155,1,155,5,0,99,2,0,14,0"""

"""
An Intcode program is a list of integers separated by commas (like 1,0,0,3,99). To run one, start by looking at the first integer (called position 0). Here, you will find an opcode - either 1, 2, or 99. The opcode indicates what to do; for example, 99 means that the program is finished and should immediately halt. Encountering an unknown opcode means something went wrong.

Opcode 1 adds together numbers read from two positions and stores the result in a third position. The three integers immediately after the opcode tell you these three positions - the first two indicate the positions from which you should read the input values, and the third indicates the position at which the output should be stored.

For example, if your Intcode computer encounters 1,10,20,30, it should read the values at positions 10 and 20, add those values, and then overwrite the value at position 30 with their sum.

Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them. Again, the three integers after the opcode indicate where the inputs and outputs are, not their values.

Once you're done processing an opcode, move to the next one by stepping forward 4 positions.
"""
def Intcode(opcodes):
	if isinstance(opcodes, str):
		opcodes = parse_opcodes(opcodes)
	for i in range(0, len(opcodes), 4):
		opcode = opcodes[i]
		# print i, opcode
		if opcode == 99:
			break

		pos1 = opcodes[i + 1]
		pos2 = opcodes[i + 2]
		position = opcodes[i + 3]

		if opcode == 1:
			opcodes[position] = opcodes[pos1] + opcodes[pos2]
		if opcode == 2:
			opcodes[position] = opcodes[pos1] * opcodes[pos2]
	
	return opcodes


def parse_opcodes(opcodes):
	return map(int, opcodes.split(","))
	

"""
Here are the initial and final states of a few more small programs:

1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.
"""
if __name__ == '__main__':
	assert(parse_opcodes('1,10,20,30') == [1,10,20,30])
	assert(Intcode('1,0,0,0,99') == [2,0,0,0,99])
	assert(Intcode('2,3,0,3,99') == [2,3,0,6,99])
	assert(Intcode('2,4,4,5,99,0') == [2,4,4,5,99,9801])
	assert(Intcode('1,1,1,4,99,5,6,0,99') == [30,1,1,4,2,5,6,0,99])
	
	print 'Day 2 tests passed'
	
	"""
	Once you have a working computer, the first step is to restore the gravity assist program (your puzzle input) to the "1202 program alarm" state it had just before the last computer caught fire. To do this, before running the program, replace position 1 with the value 12 and replace position 2 with the value 2. What value is left at position 0 after the program halts?
	"""
	opcodes = parse_opcodes(inputs)
	opcodes[1] = 12
	opcodes[2] = 2
	opcodes = Intcode(opcodes)
	print opcodes[0]