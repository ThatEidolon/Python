import socket
# import JourneymanStringServer

def journeyman1(str_list , item):

# 1.1) Take two arguments, a list and an integer. The list is a series 
# of strings; one of those strings will be the filename, the others will 
# be the file contents. The integer is the location in the list of the file 
# name. (Write each string to a separate line)

# list:
# a 0 <-contents
# b 1 <-contents
# c 2 <-contents
# d 3 <-contents
# e 4 <- filename
# f 5 <-contents

# item:
# 4

    # open a new file object with name being the name identified by item
    new_file = open(str(str_list[item]), 'w+')
    
    # remove the filename from the list
    str_list = str_list[:item] + str_list[item + 1:]

    # start writing out the list
    for line in str_list:
        new_file.write(str(line))

    # close file
    new_file.close()

    return


'''1.2) Write a function which takes a single integer as an argument and 
returns the sum of every integer up to and including that number, use a 
generator.'''

def sum_generator(final_num):
    for i in range(final_num):
        yield i

def journeyman2(final_num):
    #return sum(range(final_num+1))
    total = 0
    for i in sum_generator(final_num+1):
        total += i
    return total



'''1.3) Write a python script which connects to the included server 
on port 50001 and returns the message it receives.'''
def journeyman3():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 50001))
    recv_len = 1
    while recv_len:
        data = s.recv(1028)
        recv_len = len(data)
        print "Received: %s" % str(data)
    s.close()
    return


'''1.4) Create a class called person, with height, weight, hair color, 
and eye color fields, then implement it to describe yourself.'''
def journeyman4():
    return
    
