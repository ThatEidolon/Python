import operator

saved_string = ''

def remove_letter(): #Remove a selected letter from a string
    base_string = str(raw_input("Enter String: "))
    letter_remove = str(raw_input("Enter Letter: "))

    letter_remove = letter_remove[0]
    print "New String: %s" % base_string.strip(letter_remove)
    return

def num_compare(): #Compare 2 numbers to determine the larger
    print "Number Compare"
    num1 = int(raw_input("Enter First Number: "))
    num2 = int(raw_input("Enter Second Number: "))
    if num1 > num2 :
        print "First number is larger"
    elif num1 < num2 :
        print "Second number is larger"
    else :
        print "The numbers are equal"
    return

def print_string(): #Print the previously stored string
    print "String: %s" % saved_string
    return

def calculator(): #Basic Calculator (addition, subtraction, multiplication, division)
    print "Calculator"
    num1 = int(raw_input("Enter the First Number: "))
    sign = str(raw_input("Enter the Action: "))
    num2 = int(raw_input("Enter the Second Number: "))
    sign_dict = {"+" : operator.add, "-" : operator.sub, "*" : operator.mul, "\\" : operator.div}
    print sign_dict[sign](num1, num2)
    return
    
    
def accept_and_store(): #Accept and store a string
    global saved_string
    saved_string = str(raw_input("Enter String: "))
    return

def main(): #menu goes here

# opt_list contains a list of function pointers
    opt_list = [accept_and_store,
                calculator,
                print_string,
                num_compare,
                remove_letter]
    while True:
        print "Select Option:"
        print "1\tAccept and Store"
        print "2\tCalculator"
        print "3\tPrint Stored String"
        print "4\tNumber Comparison"
        print "5\tLetter Remover"
    
        opt_choice = int(raw_input("Enter your selection: "))
        opt_choice -= 1
    
        # call the funtion from opt_list
        opt_list[opt_choice]()
    return

main()
