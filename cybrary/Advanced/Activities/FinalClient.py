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
    return
    
def create_file(filename, data): #ctypes
    return

def recv_data(sock): #Implement a networking protocol
    return
    
def send_data(sock,data): #Implement a networking protocol
    return
    
def send_file_contents(file_name,usersock): #DOWNLOAD
    return

def receive_file_contents(file_name,usersock):#UPLOAD
    return 
    
def main():
    return
            
main()
            
            
            
