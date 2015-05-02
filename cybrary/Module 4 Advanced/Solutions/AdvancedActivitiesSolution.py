from ctypes import *
from time import sleep #need for multithreading
import threading, re

'''2.1 Ctypes: Write a function which takes two arguments, title and body
and creates a MessageBox with those arguments'''
def python_message_box(title = '' , body = ''):
    windll.User32.MessageBoxA(0,body,title,4)
    return


'''2.2 Ctypes: Write a function which takes two arguments, filename and
data and creates a file with that data written to it'''
def python_create_file(filename = '' , data = ''):
    file_handle = windll.Kernel32.CreateFileA(filename, 0x10000000, 0, 0, 4, 0x80, 0)
    written_data = c_int(0)
    windll.Kernel32.WriteFile(file_handle, data, len(data), byref(written_data), 0)
    windll.Kernel32.CloseHandle(file_handle)
    return
    

'''2.3 Ctypes: Write a function which takes one argument, a filename,
and prints the data from that file'''
def python_read_file(filename = ''):
    file_handle = windll.Kernel32.CreateFileA(filename, 0x10000000, 0, 0, 4, 0x80, 0)
    data = create_string_buffer(4096)
    read_data = c_int(0)
    windll.Kernel32.ReadFile(file_handle,byref(data),4096,byref(read_data),0)
    print data.value
    return

'''2.4 Regex: Write a regular expression to search a data block for a 
string contained in <> (html-style) brackets. IE: <span color=black>'''
def regex_html(data):
    html_match = re.compile("<.*>")
    html_results = re.search(html_match, data)
    print data
    print html_results.group()
    return
    

'''2.5 Regex: Write a regular expression to search a data block for 
phone numbers in the form of (xxx) xxx-xxxx'''
def regex_phone(data):
    phone_match = re.compile("\(\d{3}\) \d{3}-\d{4}")
    phone_results = re.search(phone_match, data)
    print data
    print phone_results.group()
    return

'''2.6 Regex: Write a regular expression to find every instance of the 
phrase "Nobody expects" and replace it with "The Spanish Inquisition"'''
def monty_python(data):
    ne_string = re.compile("Nobody expects")
    print data
    data = re.sub(ne_string, "The Spanish Inquisition", data)
    print data
        
    return


'''2.7 Multi-threading: Write a function which runs this entire program,
each function getting its own thread.'''
def multiple_threads():
    functions_list = [ python_message_box,
                    python_create_file,
                    python_read_file,
                    regex_html,
                    regex_phone,
                    monty_python]
                    
    args_list = [  ("Hello","World!"),
                ("Test.txt","IT WORKED!"),
                ("Test.txt",),
                ("ajfskdfajlsdhja;lkj<HTMLDATA>dsafsa;dfa",),
                ("kdsj;aifhjiodsh(555) 555-5555dsl'kaf;kadsjf",),
                ("Nobody expects",)]
                
    threads_list = []
    
    for i in range(len(functions_list)):
        threads_list.append(threading.Thread(None, functions_list[i],None,args_list[i]))
    
    for i in threads_list:
        i.start()
        sleep(1)

def main():
    multiple_threads()
    
main()






