from day2_1 import parse_opcodes
from day5_2 import Intcode
from day7_1 import inputs, amp_circuit
from itertools import permutations

"""
"""
class AmplifierController(Intcode):

	def __init__(self, opcodes):
		if isinstance(opcodes, str):
			self.opcodes = parse_opcodes(opcodes)
		else:
			self.opcodes = opcodes
		self.instruction_pointer = 0

	def run(self, *arg):
		arg_index = 0
		while (True):
			instruction = self.opcodes[self.instruction_pointer]
			instruction = str(instruction).rjust(5, '0')

			opcode = instruction[3:]
			
			if opcode == '99':
				break

			arg1_mode = instruction[2]
			arg2_mode = instruction[1]
			arg3_mode = instruction[0]

			# 01 and 02 are operations that take 3 parameters
			if opcode == '01' or opcode == '02':
				arg1 = self.opcodes[self.instruction_pointer + 1]
				arg2 = self.opcodes[self.instruction_pointer + 2]
				position = self.opcodes[self.instruction_pointer + 3]

				arg1_val = self.arg_val(self.opcodes, arg1, arg1_mode)
				arg2_val = self.arg_val(self.opcodes, arg2, arg2_mode)

				if opcode == '01':
					self.opcodes[position] = arg1_val + arg2_val
				if opcode == '02':
					self.opcodes[position] = arg1_val * arg2_val
				self.instruction_pointer += 4

			"""
				Opcode 3 takes a single integer as input and saves it to the position given by its only parameter. For example, the instruction 3,50 would take an input value and store it at address 50.
			"""
			if opcode == '03':
				arg1 = self.opcodes[self.instruction_pointer + 1]
				self.opcodes[arg1] = arg[arg_index]
				arg_index += 1
				self.instruction_pointer += 2
	
			"""
				Opcode 4 outputs the value of its only parameter. For example, the instruction 4,50 would output the value at address 50.
			"""
			if opcode == '04':
				arg1 = self.opcodes[self.instruction_pointer + 1]
				self.instruction_pointer += 2
				return self.opcodes[arg1]
			
			"""
				Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
			"""
			if opcode == '05':
				arg1 = self.opcodes[self.instruction_pointer + 1]
				arg2 = self.opcodes[self.instruction_pointer + 2]
				
				arg1_val = self.arg_val(self.opcodes, arg1, arg1_mode)
				arg2_val = self.arg_val(self.opcodes, arg2, arg2_mode)
				
				if arg1_val != 0:
					self.instruction_pointer = arg2_val
				else:
					self.instruction_pointer += 3
			
			"""
				Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
			"""
			if opcode == '06':
				arg1 = self.opcodes[self.instruction_pointer + 1]
				arg2 = self.opcodes[self.instruction_pointer + 2]
				
				arg1_val = self.arg_val(self.opcodes, arg1, arg1_mode)
				arg2_val = self.arg_val(self.opcodes, arg2, arg2_mode)
				
				if arg1_val == 0:
					self.instruction_pointer = arg2_val
				else:
					self.instruction_pointer += 3
			
			"""
				Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
			"""
			if opcode == '07':
				arg1 = self.opcodes[self.instruction_pointer + 1]
				arg2 = self.opcodes[self.instruction_pointer + 2]
				position = self.opcodes[self.instruction_pointer + 3]
				
				arg1_val = self.arg_val(self.opcodes, arg1, arg1_mode)
				arg2_val = self.arg_val(self.opcodes, arg2, arg2_mode)
				
				if arg1_val < arg2_val:
					self.opcodes[position] = 1
				else:
					self.opcodes[position] = 0
				self.instruction_pointer += 4
			
			"""
				Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
			"""
			if opcode == '08':
				arg1 = self.opcodes[self.instruction_pointer + 1]
				arg2 = self.opcodes[self.instruction_pointer + 2]
				position = self.opcodes[self.instruction_pointer + 3]
				
				arg1_val = self.arg_val(self.opcodes, arg1, arg1_mode)
				arg2_val = self.arg_val(self.opcodes, arg2, arg2_mode)
				
				if arg1_val == arg2_val:
					self.opcodes[position] = 1
				else:
					self.opcodes[position] = 0
				self.instruction_pointer += 4

		raise AmplifierControllerHalt()


class AmplifierControllerHalt(RuntimeError):
	pass


def amp_circuit_feedback_loop(opcodes, phase_settings):
	input_signal = 0
	count = 0
	amplifiers = []
	for i in range(0, len(phase_settings)):
		amplifiers.append(AmplifierController(opcodes))
	
	for i in range(0, len(phase_settings)):
		input_signal = amplifiers[i].run(int(phase_settings[i]), input_signal)
	
	while True:
		i = count % len(phase_settings)
		count += 1
		try:
			input_signal = amplifiers[i].run(input_signal)
		except AmplifierControllerHalt as e:
			break

	return input_signal


def find_highest_signal(opcodes):
	all_phase_settings = [''.join(p) for p in permutations('56789')]
	highest_signal = 0
	for phase_setting in all_phase_settings:
		signal = amp_circuit_feedback_loop(opcodes, phase_setting)
		if signal > highest_signal:
			highest_signal = signal
	return highest_signal


if __name__ == '__main__':
	opcodes = '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'
	assert amp_circuit_feedback_loop(opcodes, '98765') == 139629729
	
	opcodes = '3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10'
	assert amp_circuit_feedback_loop(opcodes, '97856') == 18216
	
	print 'Day 7 tests completed'
	print
	print find_highest_signal(inputs)