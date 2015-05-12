import socket
import threading

'''
1.5) Python Journeyman: Write a Python server which:
	receives a connection from the included client (JourneymanFinal.py)
	stores received data in a file, then adds the file to a list
	returns the data from the file when requested
	deals with errors and missing files
'''

def configure_server():
    # configure server to listen on localhost port 50002, and listen for up to five clients
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 50002))
    s.listen(5)
    return s

def server_loop():
    server_socket = configure_server()
    while True:
        conn, addr = server_socket.accept()
        client_thread = threading.Thread(target=client_handler, args=(conn,))
        # setting daemon to true is required to terminated with ctrl-c
        client_thread.daemon = True
        client_thread.start()
    return

def save_data(filename, data):
    # save data to filename
    return

def read_data(filename):
    # read from filename and return data
    data = ''
    return data

def client_handler(client_socket):
    data = client_socket.recv(4096)    
    mode = str(data[:4])
    file_name = str(data[4:9]) # the fuck?!
    contents = str(data[9:])
    print "Mode: %s" % mode
    print "File Name: %s" % file_name
    print "Contents: %s" % contents
    client_socket.close()
    return

def receive_data(some_socket):
    data = ''
    data = some_socket.recv(4096)
    return data

def send_data(some_socket, data):
    return some_socket

def main():
    # this is quick and dirty and will be a constant loop
    
    # configure a new server and save it as server socket
    server_loop()
    return

if __name__ == "__main__":
    main()