import socket
'''
1.5) Python Journeyman: Write a Python server which:
	receives a connection from the included client (JourneymanFinal.py)
	stores received data in a file, then adds the file to a list
	returns the data from the file when requested
	deals with errors and missing files
'''

def configure_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 50001))
    return s

def main():


main()
