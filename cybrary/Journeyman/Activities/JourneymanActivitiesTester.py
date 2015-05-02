from JourneymanActivities import *
import os

def journeymantest1():
    str_list_list = [
                    ['a','b','c','d','e'] ,
                    ['this' , 'is' , 'a' , 'chimpanzee' , 'test'] ,
                    ['item1' , 'item2' , 'item3' , 'item4' , 'item5']
                    ]
    integer_list = [1,3,0]
    for i in range(len(str_list_list)):
        working_list = []
        for item in str_list_list[i]:
            working_list.append(item)
        journeyman1(str_list_list[i] , integer_list[i])
        f = open(str_list_list[i][integer_list[i]])
        working_list.remove(working_list[integer_list[i]])
        for j in range(4):
            line = f.read(len(working_list[j]))
            if line != working_list[j]:
                print "Failed: %s != %s" % (line , working_list[j])
                return -1
            print line
        print "\n"
        f.close()
        os.remove(str_list_list[i][integer_list[i]])
    print "Test 1: SUCCESS\n"
    return 0

def journeymantest2():
    max_list = [10,4,1000,35]
    for i in max_list:
        if journeyman2(i) != sum(range(i+1)):
            print "Failed: %d != %d" % (journeyman2(i) , sum(range(i+1)))
            return -1
        print "%d\t:\t%d" % (i , journeyman2(i))
    print "Test 2: SUCCESS\n"
    return 0

def journeymantest3():
    message_list = ['alpha' , 'bravo' , 'charlie' , 'delta']
    
    for i in message_list:
        res = journeyman3()
        if res != i:
            print "Failed: %s != %s" % (res , i)
            return -1
        print res
    print "Test 3: SUCCESS\n"

def journeymantest4():
    journeyman4()

def main():
    journeymantest1()
    journeymantest2()
    #journeymantest3()
    journeymantest4()

main()
