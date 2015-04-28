from Apprentice_Activities import *

def activity01test():
	tests = {2 : 'Even' , 17 : 'Odd' , 1 : 'Odd' , 5 : 'Odd'}
	print "Starting Test 1..."
	for i in tests:
		return_string = activity01(i)
		if tests[i] != return_string:
			print "Failed: Input %d\nExpected: %s\nReceived: %s" % (i, tests[i], return_string)
			return -1
		else:
			print "Correct:\t%d\t\t=\t%s" % (i, return_string)
	return 0
	
def activity02test():
	tests = [[1,2,3] , [4,19,23] , [0,0,0] , [3,6,9]]
	print "\nStarting Test 2..."
	for i in tests:
		return_value = activity02(i[0], i[1])
		if return_value != i[2]:
			print "Failed: Inputs: %d, %d\nExpected: %d\nRecieved: %d" % (i[0], i[1], i[2])
			return -1
		else:
			print "Correct:\t%d+%d\t\t=\t%d" % (i[0], i[1], i[2]) 
	return 0
	
def activity03test():
	tests = [[[1,2,3,4] , 2] , [[1,3,5,7] , 0] , [[2,4,6,9] , 3] , [[1,2,6,7] , 2]]
	print "\nStarting Test 3..."
	for i in tests:
		return_value = activity03(i[0])
		if return_value != i[1]:
			print "Failed: Input: %s\nExpected: %d\nReceived: %d" % (str(i[0]), i[1], return_value)
			return -1
		else:
			print "Correct:\t%s\t=\t%d" % (str(i[0]), return_value)
	return 0
	
def activity04test():
	tests = {'string' : 'gnirts' , 'racecar' : 'racecar' , 'test' : 'tset' , 'success' : 'sseccus'}
	print "\nStarting Test 4..."
	for i in tests:
		return_string = activity04(i)
		if tests[i] != return_string:
			print "Failed: Input: %s\nExpected: %s\nReceived: %s\n" % (i, tests[i], return_string)
			return -1
		else:
			print "Correct:\t%s\t\t=\t%s" % (i, tests[i])
	return 0

def main():
	test_list = [activity01test(), activity02test(), activity03test(), activity04test()]
	for i in test_list:
		if i != 0:
			return
	
	
main()
