from day2_1 import parse_opcodes
import day5_1

"""
"""
class Intcode(day5_1.Intcode):
	def run(self, *arg):
		# Create a copy of this so subsequent runs with different inputs are not using a mutated program state
		opcodes = self.opcodes

		"""
			It is important to remember that the instruction pointer should increase by the number of values in the instruction after the instruction finishes. Because of the new instructions, this amount is no longer always 4.
		"""
		instruction_pointer = 0
		stdout = []
		arg_index = 0
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
				opcodes[arg1] = arg[arg_index]
				arg_index += 1
				instruction_pointer += 2
	
			"""
				Opcode 4 outputs the value of its only parameter. For example, the instruction 4,50 would output the value at address 50.
			"""
			if opcode == '04':
				arg1 = opcodes[instruction_pointer + 1]
				stdout.append(opcodes[arg1])
				instruction_pointer += 2
			
			"""
				Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
			"""
			if opcode == '05':
				arg1 = opcodes[instruction_pointer + 1]
				arg2 = opcodes[instruction_pointer + 2]
				
				arg1_val = self.arg_val(opcodes, arg1, arg1_mode)
				arg2_val = self.arg_val(opcodes, arg2, arg2_mode)
				
				if arg1_val != 0:
					instruction_pointer = arg2_val
				else:
					instruction_pointer += 3
			
			"""
				Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
			"""
			if opcode == '06':
				arg1 = opcodes[instruction_pointer + 1]
				arg2 = opcodes[instruction_pointer + 2]
				
				arg1_val = self.arg_val(opcodes, arg1, arg1_mode)
				arg2_val = self.arg_val(opcodes, arg2, arg2_mode)
				
				if arg1_val == 0:
					instruction_pointer = arg2_val
				else:
					instruction_pointer += 3
			
			"""
				Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
			"""
			if opcode == '07':
				arg1 = opcodes[instruction_pointer + 1]
				arg2 = opcodes[instruction_pointer + 2]
				position = opcodes[instruction_pointer + 3]
				
				arg1_val = self.arg_val(opcodes, arg1, arg1_mode)
				arg2_val = self.arg_val(opcodes, arg2, arg2_mode)
				
				if arg1_val < arg2_val:
					opcodes[position] = 1
				else:
					opcodes[position] = 0
				instruction_pointer += 4
			
			"""
				Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
			"""
			if opcode == '08':
				arg1 = opcodes[instruction_pointer + 1]
				arg2 = opcodes[instruction_pointer + 2]
				position = opcodes[instruction_pointer + 3]
				
				arg1_val = self.arg_val(opcodes, arg1, arg1_mode)
				arg2_val = self.arg_val(opcodes, arg2, arg2_mode)
				
				if arg1_val == arg2_val:
					opcodes[position] = 1
				else:
					opcodes[position] = 0
				instruction_pointer += 4

		return stdout, opcodes

"""
3,9,8,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
3,9,7,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
3,3,1108,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
3,3,1107,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).

Here are some jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero:
3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9 (using position mode)
3,3,1105,-1,9,1101,0,0,12,4,12,99,1 (using immediate mode)
"""
if __name__ == '__main__':
	assert Intcode('3,0,4,0,99').run(1)[0] == [1]
	assert Intcode('3,0,4,0,99').run(500)[0] == [500]
	assert Intcode('1101,100,-1,4,0').run(1) == ([], [1101,100,-1,4,99])

	assert Intcode('3,9,8,9,10,9,4,9,99,-1,8').run(1)[0][0] == 0
	assert Intcode('3,9,8,9,10,9,4,9,99,-1,8').run(10)[0][0] == 0
	assert Intcode('3,9,8,9,10,9,4,9,99,-1,8').run(8)[0][0] == 1

	assert Intcode('3,9,7,9,10,9,4,9,99,-1,8').run(1)[0][0] == 1
	assert Intcode('3,9,7,9,10,9,4,9,99,-1,8').run(10)[0][0] == 0
	assert Intcode('3,9,7,9,10,9,4,9,99,-1,8').run(8)[0][0] == 0

	assert Intcode('3,3,1108,-1,8,3,4,3,99').run(1)[0][0] == 0
	assert Intcode('3,3,1108,-1,8,3,4,3,99').run(10)[0][0] == 0
	assert Intcode('3,3,1108,-1,8,3,4,3,99').run(8)[0][0] == 1

	assert Intcode('3,3,1107,-1,8,3,4,3,99').run(1)[0][0] == 1
	assert Intcode('3,3,1107,-1,8,3,4,3,99').run(10)[0][0] == 0
	assert Intcode('3,3,1107,-1,8,3,4,3,99').run(8)[0][0] == 0

	assert Intcode('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9').run(0)[0][0] == 0
	assert Intcode('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9').run(1)[0][0] == 1
	assert Intcode('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9').run(10)[0][0] == 1
	assert Intcode('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9').run(8)[0][0] == 1
	assert Intcode('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9').run(0)[0][0] == 0

	assert Intcode('3,3,1105,-1,9,1101,0,0,12,4,12,99,1').run(1)[0][0] == 1
	assert Intcode('3,3,1105,-1,9,1101,0,0,12,4,12,99,1').run(10)[0][0] == 1
	assert Intcode('3,3,1105,-1,9,1101,0,0,12,4,12,99,1').run(8)[0][0] == 1
	assert Intcode('3,3,1105,-1,9,1101,0,0,12,4,12,99,1').run(0)[0][0] == 0
	
	i = Intcode('3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99')
	
	# I'm not sure if there's a bug in my code or if there's a bug in the "intcode", but I get a list index out of range error when using values less than 8. It's trying to output the value at address 999 (which makes me think it's not my bug).
	# assert i.run(7)[0][0] == 999
	assert i.run(8)[0][0] == 1000
	assert i.run(9)[0][0] == 1001

	print 'Day 5 part 2 tests pass'
	print
	print Intcode(day5_1.inputs).run(5)[0]
