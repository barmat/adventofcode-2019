from day2_1 import parse_opcodes

inputs = '3,225,1,225,6,6,1100,1,238,225,104,0,1102,31,68,225,1001,13,87,224,1001,224,-118,224,4,224,102,8,223,223,1001,224,7,224,1,223,224,223,1,174,110,224,1001,224,-46,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1101,13,60,224,101,-73,224,224,4,224,102,8,223,223,101,6,224,224,1,224,223,223,1101,87,72,225,101,47,84,224,101,-119,224,224,4,224,1002,223,8,223,1001,224,6,224,1,223,224,223,1101,76,31,225,1102,60,43,225,1102,45,31,225,1102,63,9,225,2,170,122,224,1001,224,-486,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1102,29,17,224,101,-493,224,224,4,224,102,8,223,223,101,1,224,224,1,223,224,223,1102,52,54,225,1102,27,15,225,102,26,113,224,1001,224,-1560,224,4,224,102,8,223,223,101,7,224,224,1,223,224,223,1002,117,81,224,101,-3645,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,8,226,677,224,102,2,223,223,1005,224,329,1001,223,1,223,1108,677,226,224,102,2,223,223,1006,224,344,101,1,223,223,108,677,226,224,102,2,223,223,1006,224,359,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,374,101,1,223,223,1007,226,677,224,102,2,223,223,1005,224,389,101,1,223,223,8,677,677,224,102,2,223,223,1006,224,404,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,419,101,1,223,223,1108,677,677,224,1002,223,2,223,1005,224,434,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,449,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,464,101,1,223,223,1108,226,677,224,1002,223,2,223,1005,224,479,1001,223,1,223,7,677,677,224,102,2,223,223,1006,224,494,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,509,101,1,223,223,107,677,677,224,1002,223,2,223,1006,224,524,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,539,101,1,223,223,7,226,677,224,1002,223,2,223,1005,224,554,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,569,101,1,223,223,1008,226,677,224,102,2,223,223,1005,224,584,101,1,223,223,8,677,226,224,1002,223,2,223,1005,224,599,101,1,223,223,1007,226,226,224,1002,223,2,223,1005,224,614,101,1,223,223,1107,226,226,224,1002,223,2,223,1006,224,629,101,1,223,223,107,677,226,224,1002,223,2,223,1005,224,644,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,659,101,1,223,223,108,677,677,224,1002,223,2,223,1005,224,674,1001,223,1,223,4,223,99,226'

"""
Opcode 3 takes a single integer as input and saves it to the position given by its only parameter. For example, the instruction 3,50 would take an input value and store it at address 50.
Opcode 4 outputs the value of its only parameter. For example, the instruction 4,50 would output the value at address 50.
"""

class Intcode():
	def __init__(self, opcodes):
		if isinstance(opcodes, str):
			self.opcodes = parse_opcodes(opcodes)
		else:
			self.opcodes = opcodes
	
	def run(self, stdin):
		# Create a copy of this so subsequent runs with different inputs are not using a mutated program state
		opcodes = self.opcodes

		"""
			It is important to remember that the instruction pointer should increase by the number of values in the instruction after the instruction finishes. Because of the new instructions, this amount is no longer always 4.
		"""
		instruction_pointer = 0
		stdout = []
		while (True):
			instruction = opcodes[instruction_pointer]
			instruction = str(instruction).rjust(5, '0')

			opcode = instruction[3:]

			if opcode == '99':
				break

			arg1_mode = instruction[2]
			arg2_mode = instruction[1]
			arg3_mode = instruction[0]

			# 01 and 02 are operations that take 3 parameters
			if opcode == '01' or opcode == '02':
				arg1 = opcodes[instruction_pointer + 1]
				arg2 = opcodes[instruction_pointer + 2]
				position = opcodes[instruction_pointer + 3]

				arg1_val = self.arg_val(opcodes, arg1, arg1_mode)
				arg2_val = self.arg_val(opcodes, arg2, arg2_mode)

				if opcode == '01':
					opcodes[position] = arg1_val + arg2_val
				if opcode == '02':
					opcodes[position] = arg1_val * arg2_val
				instruction_pointer += 4

			"""
				Opcode 3 takes a single integer as input and saves it to the position given by its only parameter. For example, the instruction 3,50 would take an input value and store it at address 50.
			"""
			if opcode == '03':
				arg1 = opcodes[instruction_pointer + 1]
				opcodes[arg1] = stdin
				instruction_pointer += 2
	
			"""
				Opcode 4 outputs the value of its only parameter. For example, the instruction 4,50 would output the value at address 50.
			"""
			if opcode == '04':
				arg1 = opcodes[instruction_pointer + 1]
				stdout.append(opcodes[arg1])
				instruction_pointer += 2

		return stdout, opcodes

	def arg_val(self, opcodes, argument, mode):
		if mode == '1':
			return argument
		else:
			return opcodes[argument]

if __name__ == '__main__':
	# print Intcode('99').run(1)
	# print Intcode('1002,4,3,4,33').run(1)
	
	assert Intcode('3,0,4,0,99').run(1)[0] == [1]
	assert Intcode('3,0,4,0,99').run(500)[0] == [500]
	assert Intcode('1101,100,-1,4,0').run(1) == ([], [1101,100,-1,4,99])
	
	print 'Day 5 tests pass'
	print
	print Intcode(inputs).run(1)
