import socket
import threading

HOST = 'localhost'
PORT = 50002
OPTIONS = ['SAVE', 'LOAD']

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
    s.bind((HOST, PORT))
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
    with open(filename, 'w+') as f:
        f.write(data)


def send_file(some_socket, filename):
    # read from filename and return data
    try:
        with open(filename) as f:
            some_socket.send(f.readline())
    except:
        some_socket.send("File Not Found")


def client_handler(client_socket):
    data = client_socket.recv(4096)
    mode = str(data[:4])
    file_name = str(data[4:9])  # the fuck?!
    contents = str(data[9:])
    if mode == OPTIONS[0]:  # save
        save_data(file_name, contents)
    elif mode == OPTIONS[1]:  # load
        send_file(client_socket, file_name)
    client_socket.close()
    return


def main():
    # this is quick and dirty and will be a constant loop
    # configure a new server and save it as server socket
    server_loop()
    return


if __name__ == "__main__":
    main()
