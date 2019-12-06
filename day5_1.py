from day2_1 import parse_opcodes

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
