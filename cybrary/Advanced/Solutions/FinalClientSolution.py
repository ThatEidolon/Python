'''
The final activity for the Advanced Python section is a drive-wide FTP-like
tool. You should be able to receive multiple connections, each on their 
own thread. You should take several commands:
DRIVESEARCH <filename>
    DRIVESEARCH looks for the given filename across the entire drive. If
    it finds the file, it sends back the drive location.
DIRSEARCH <directory> <filename>
    DIRSEARCH looks for the file in the given directory or its 
    subdirectories. If it finds the file, it sends back the location.
DOWNLOAD <filename>
    DOWNLOAD requires the full file path, or at least the relative path,
    of the file. It sends the contents of the file across the network.
UPLOAD <filename>
    UPLOAD requires the full file path, or at least the relative path,
    where the user wants to locate the file. It reads the file contents
    from across the network connection.
CLOSE
    CLOSE ends the connection
    
This activity will require you to use multithreading, regular
expressions, and some libraries with which you're unfamiliar. ENJOY!
'''

import os, re, socket, threading, struct, sys
from ctypes import *

def read_file(filename): #ctypes
    file_handle = windll.Kernel32.CreateFileA(filename, 0x10000000, 0, 0, 3, 0x80, 0)
    if(file_handle == -1):
        return -1
        
    data = create_string_buffer(4096)
    data_read = c_int(0)
    
    bool_success = windll.Kernel32.ReadFile(file_handle, byref(data), 4096, byref(data_read), 0)
    windll.Kernel32.CloseHandle(file_handle)
    if(bool_success == 0):
        return -1
        
    return data.value
    
def create_file(filename, data): #ctypes
    file_handle = windll.Kernel32.CreateFileA(filename, 0x10000000, 0, 0, 2, 0x80, 0)
    if(file_handle == -1):
        return -1
    
    data_written = c_int(0)
    bool_success = windll.Kernel32.WriteFile(file_handle, data, len(data), byref(data_written), 0)
    windll.Kernel32.CloseHandle(file_handle)
    if (bool_success == 0):
        return -1
    return

def recv_data(sock): #Implement a networking protocol
    data_len, = struct.unpack("!I",sock.recv(4))
    return sock.recv(data_len)
    
def send_data(sock,data): #Implement a networking protocol
    data_len = len(data)
    sock.send(struct.pack("!I",data_len))
    sock.send(data)
    return
    
def send_file_contents(file_name,usersock): #DOWNLOAD
    send_data(usersock,read_file(file_name))
    return

def receive_file_contents(file_name,usersock):#UPLOAD
    if (create_file(file_name, recv_data(usersock)) == -1):
        send_data(usersock, "File Creation Failed")
    return 
    
def main():
    command_list = ["DRIVESEARCH",
                    "DIRSEARCH",
                    "DOWNLOAD",
                    "UPLOAD",
                    "CLOSE"]
                    
    cont = True
                    
    if len(sys.argv) < 2:
        print "Usage: %s [ADDRESS]" % sys.argv[0]
        exit()
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((sys.argv[1],55555))
    except:
        print "Cannot connect to %s" % sys.argv[1]
    
    while(cont != False):
        command = raw_input(recv_data(sock)).upper()
        send_data(sock, command)
        if command not in command_list:
            print recv_data(sock)
            print command_list
            
        elif command == "DRIVESEARCH":
            file_name = raw_input(recv_data(sock))
            send_data(sock, file_name)
            print recv_data(sock)
            
        elif command == "DIRSEARCH":
            file_name = raw_input(recv_data(sock))
            send_data(sock, file_name)
            print recv_data(sock)
            
        elif command == "DOWNLOAD":
            file_name = raw_input(recv_data(sock))
            send_data(sock, file_name)
            receive_file_contents(raw_input("Local Filename: "),sock)
            
        elif command == "UPLOAD":
            file_name = raw_input(recv_data(sock))
            new_file_name = raw_input("File to create: ")
            send_data(sock, new_file_name)
            send_file_contents(file_name, sock)
            
        elif command == "CLOSE":
            cont = False
            
    sock.close()
            
main()
            
            
            
