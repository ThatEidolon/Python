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
import subprocess, socket, time, struct
from _winreg import *

def recv_data(sock):
    data_len, = struct.unpack("!I",sock.recv(4))
    return sock.recv(data_len)
    
def send_data(sock,data):
    data_len = len(data)
    sock.send(struct.pack("!I",data_len))
    sock.send(data)
    return

def create_user(name,pwd):
    return

def delete_user(name):
    return

def download_registry_key(root, path, sock):
    return

def download_file(file_name,sock):
    return
        
def gather_information(log_name,sock):
    return
    
def execute_command(cmd):
    return
    
def get_data(sock, str_to_send):
    return

def main():
    return
    
main()
    
