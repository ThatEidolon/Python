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
    
This activity will require you to use multithreading, ctypes, regular
expressions, and some libraries with which you're unfamiliar. ENJOY!
'''

import os, re, socket, threading, struct
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

def search_drive(file_name): #DRIVESEARCH
    re_obj = re.compile(file_name)
    for root, dirs, files in os.walk("C:\\"):
        for i in files:
            if(re.search(re_obj,i)):
                return os.path.join(root,i)
    return -1

def search_directory(file_name): #DIRSEARCH
    re_obj = re.compile(file_name)
    for root, dirs, files in os.walk(os.getcwd()):
        for i in files:
            if(re.search(re_obj,i)):
                return os.path.join(root,i)
    return -1

def send_file_contents(file_name,usersock,userinfo): #DOWNLOAD
    data = read_file(file_name)
    print data
    if (data == -1):
        send_data(usersock, "FILE NOT FOUND")
        return -1
    send_data(usersock,data)
    return

def receive_file_contents(file_name,usersock):#UPLOAD
    if (create_file(file_name, recv_data(usersock)) == -1):
        send_data(usersock, "File Creation Failed")
    return

def handle_connection(usersock,userinfo):
    command_list = ["DRIVESEARCH",
                    "DIRSEARCH",
                    "DOWNLOAD",
                    "UPLOAD",
                    "CLOSE"]
                    
    continue_bool = True

    while(continue_bool):
        send_data(usersock,"COMMAND: ")
        command = recv_data(usersock).upper()
        
        if (command == "DRIVESEARCH"):
            send_data(usersock, "Filename: ")
            search_results = search_drive(recv_data(usersock))
            if(search_results == -1):
                send_data(usersock, "FILE NOT FOUND")
            else:
                send_data(usersock,search_results)
            
        elif (command == "DIRSEARCH"):
            send_data(usersock, "Filename: ")
            search_results = search_directory(recv_data(usersock))
            if (search_results == -1):
                send_data(usersock, "FILE NOT FOUND")
            else:
                send_data(usersock, search_results)
            
        elif (command == "DOWNLOAD"):
            send_data(usersock, "Filename: ")
            send_file_contents(recv_data(usersock),usersock,userinfo)
            
        elif (command == "UPLOAD"):
            send_data(usersock, "Filename: ")
            receive_file_contents(recv_data(usersock),usersock)
            
        elif (command == "CLOSE"):
            continue_bool = False
            
        else:
            send_data(usersock, "INVALID COMMAND")
    return

def main():
    
    while(True):
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_sock.bind(('',55555))
        server_sock.listen(8)
        usersock, userinfo = server_sock.accept()
        
        conn_thread = threading.Thread(None, handle_connection, None, (usersock,userinfo))
        conn_thread.start()
        
    
    return

main()
