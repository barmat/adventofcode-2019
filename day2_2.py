from day2_1 import Intcode, inputs, parse_opcodes

"""
"With terminology out of the way, we're ready to proceed. To complete the gravity assist, you need to determine what pair of inputs produces the output 19690720."

The inputs should still be provided to the program by replacing the values at addresses 1 and 2, just like before. In this program, the value placed in address 1 is called the noun, and the value placed in address 2 is called the verb. Each of the two input values will be between 0 and 99, inclusive.

Once the program has halted, its output is available at address 0, also just like before. Each time you try a pair of inputs, make sure you first reset the computer's memory to the values in the program (your puzzle input) - in other words, don't reuse memory from a previous attempt.

Find the input noun and verb that cause the program to produce the output 19690720. What is 100 * noun + verb? (For example, if noun=12 and verb=2, the answer would be 1202.)
"""


def run_intcode(noun, verb):
	opcodes = parse_opcodes(inputs)
	opcodes[1] = noun
	opcodes[2] = verb
	opcodes = Intcode(opcodes)
	
	return opcodes[0]

if __name__ == '__main__':
	for noun in range(0, 99):
		for verb in range(0, 99):
			output = run_intcode(noun, verb)
			if output == 19690720:
				print 100 * noun + verb
				quit()

