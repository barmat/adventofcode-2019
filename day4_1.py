import string
"""
It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
"""

password_range = (171309, 643603)
def is_valid_password(password):
	try:
		ipass = int(password)
		valid = len(password) == 6 and (
				string.find(password, '00') != -1 or
				string.find(password, '11') != -1 or
				string.find(password, '22') != -1 or
				string.find(password, '33') != -1 or
				string.find(password, '44') != -1 or
				string.find(password, '55') != -1 or
				string.find(password, '66') != -1 or
				string.find(password, '77') != -1 or
				string.find(password, '88') != -1 or
				string.find(password, '99') != -1
			)
		if valid:
			for i in range(1, len(password)):
				if int(password[i]) < int(password[i - 1]):
					return False
			return True
			
	except ValueError as e:
		pass
	return False

"""
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
"""

if __name__ == '__main__':
	assert is_valid_password('122345')
	assert is_valid_password('111111')
	assert not is_valid_password('223450')
	assert not is_valid_password('123789')
	
	print 'Day 4 tests pass'
	
	total = 0
	for i in range(password_range[0], password_range[1] + 1):
		if is_valid_password(str(i).rjust(6, '0')):
			total += 1
	
	print total
