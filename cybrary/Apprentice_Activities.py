def activity01(num1):
	'''Determine if an input number is Even or Odd'''
	try:
		if int(num1) % 2:
			return "Odd"
		else:
			return "Even"
	except:
		return "Not a number"
		
def activity02(iv_one, iv_two):
	'''Return the sum of two input values'''
	try:		
		return int(iv_one) + int(iv_two)
	except:
		return "Does not contain only numbers"

def activity03(num_list):
	'''Given a list of integers, count how many are even'''
	count = 0
	try:
		for i in num_list:
			if not (int(i) % 2):
				count += 1
		return count
	except:
		return "List contains non-numbers"
				
	
def activity04(input_string):
	'''Return the input string, backward'''
	try:
		return input_string[::-1]
	except:
		return "Not a string"
