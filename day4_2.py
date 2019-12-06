import day4_1, string

"""
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.
"""
def is_valid_password(password):
	if day4_1.is_valid_password(password):
		return ((string.find(password, '00') != -1 and string.find(password, '000') == -1) or
			(string.find(password, '11') != -1 and string.find(password, '111') == -1) or
			(string.find(password, '22') != -1 and string.find(password, '222') == -1) or
			(string.find(password, '33') != -1 and string.find(password, '333') == -1) or
			(string.find(password, '44') != -1 and string.find(password, '444') == -1) or
			(string.find(password, '55') != -1 and string.find(password, '555') == -1) or
			(string.find(password, '66') != -1 and string.find(password, '666') == -1) or
			(string.find(password, '77') != -1 and string.find(password, '777') == -1) or
			(string.find(password, '88') != -1 and string.find(password, '888') == -1) or
			(string.find(password, '99') != -1 and string.find(password, '999') == -1))
	return False


"""
112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
"""
if __name__ == '__main__':
	assert is_valid_password('112233')
	assert not is_valid_password('123444')
	assert is_valid_password('111122')
	
	print 'Day 4 part 2 tests pass'
	
	total = 0
	for i in range(day4_1.password_range[0], day4_1.password_range[1] + 1):
		if is_valid_password(str(i).rjust(6, '0')):
			total += 1
	
	print total
	