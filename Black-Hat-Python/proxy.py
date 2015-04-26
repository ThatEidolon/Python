#!/usr/bin/python2.7

import sys
import socket
import threading

# this is a pretty hex dumping function directly taken from
# http://code.activestate.com/recipes/142812-hex-dumper/
def hexdump(src, length=16):
    result = []
    digits = 4 if isinstance(src, unicode) else 2

    for i in xrange(0, len(src), length):
        s = src[i:i+length]
        hexa = b' '.join(["%0*X" % (digits, ord(x))  for x in s])
        text = b''.join([x if 0x20 <= ord(x) < 0x7F else b'.'  for x in s])
        result.append( b"%04X   %-*s   %s" % (i, length*(digits + 1), hexa, text) )

    print b'\n'.join(result)

# main server loop for handling connections and forking a process to handler
def server_loop(local_host,local_port,remote_host,remote_port,receive_first):
    
    # create the server object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # lets see if we can stand up the server
    try:
        server.bind((local_host,local_port))
    except:
        print "[!] Failed to listen on %s:%d" % (local_host, local_port)
        print "[!] Check for other listening sockets or correct permissions"
        sys.exit(0)
    
    # listen with 5 backlogged--queued--connections
    server.listen(5)
    
    while True:
        client_socket, addr = server.accept()
        
        # print out the local connection information 
        print"[+] Received incoming connections from %s:%d" % (addr[0],addr[1])
        
        # start a new thread to talk to the remote host
        proxy_thread = threading.Thread(target=proxy_handler,args=(client_socket,remote_host,remote_port,receive_first))
        
        proxy_thread.start()

def proxy_handler(client_socket,remote_host,remote_port,receive_first):
    # connect to remote host
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        remote_socket.connect((remote_host,remote_port))
        print "[+] Remote Connection established"
    except:
        # something went wrong, eject!
        print "[!] Unable to connect to remote host, exiting"
        sys.exit(0)
    if receive_first:
        remote_buffer = receive_from(remote_socket)
        hexdump(remote_buffer)
        
        # send it to our response handler
        remote_buffer = response_handler(remote_buffer)
        
        # if we have data to send to our local client, send it
        if len(remote_buffer):
            print "[*] Sending %d bytes to localhost" % len(remote_buffer)
            client_socket.send(remote_buffer)
    # now loop sending to remote and sending to local
    while True:
        local_buffer = receive_from(client_socket)
        if len(local_buffer):
            print "[*] Received %d bytes from localhost" % len(local_buffer)
            hexdump(local_buffer)
            
            # send it to our request handler
            local_buffer = request_handler(local_buffer)
            
            # send it off to the remote host
            print "[*] Buffer = %s" % local_buffer
            remote_socket.send(local_buffer)
            print "[*] Sent to remote."
            
        # receive the response back
        remote_buffer = receive_from(remote_socket)
        
        if len(remote_buffer):
            print "[*] Received %d bytes from remote." % len(remote_buffer)
            hexdump(remote_buffer)
            
            # send it to our handler
            remote_buffer = response_handler(remote_buffer)
            
            # sent it to the local host
            client_socket.send(remote_buffer)
            print "[*] Sent to local."
            
        # if nothing left to send, close down connections
        if not len(remote_buffer) or not len(local_buffer):
            remote_socket.close()
            client_socket.close()
            print "[*] No more data, closing connections"       
            break
    
def receive_from(connection):
    buffer = ""
    
    # set a two second timeout; this my need to be adjusted
    connection.settimeout(2)
    
    try:
        # read from buffer until full, or connection times out
        while True:
            data = connection.recv(4096)
            if not data:
                break
            buffer += data
    except:
        pass
    return buffer

# handler function to modify server responses
def response_handler(remote_buffer):
    # perform packet modifications here
    return remote_buffer

# handler function to modify client requests
def request_handler(local_buffer):
    # perform packet modifications here
    return local_buffer
        
def main():
    # cursory check of command line args
    if len(sys.argv[1:]) != 5:
        print "Usage:   ./proxy.py [localhost] [localport] [remotehost] [remoteport] [receive_first]"
        print "Example: ./proxy.py 127.0.0.1 9000 10.11.132.1 9000 True"
        sys.exit(0)
    
    # set up listening parameters
    local_host = sys.argv[1]
    local_port = int(sys.argv[2])
    
    # set up remote targets
    remote_host = sys.argv[3]
    remote_port = int(sys.argv[4])
    
    # this tells our proxy to connect and receive data before sending to the remote host
    receive_first = sys.argv[5]
    
    if "True" in receive_first:
        receive_first = True
    else:
        receive_first = False
        
    # now spin up our listening socket
    server_loop(local_host,local_port,remote_host,remote_port,receive_first)
    
if __name__ == "__main__":
    main()