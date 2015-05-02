import socket
'''
1.5) Python Journeyman: Write a Python server which:
	receives a connection from the included client (JourneymanFinal.py)
	stores received data in a file, then adds the file to a list
	returns the data from the file when requested
	deals with errors and missing files
'''

class datasave:
    def __init__(self, name = '' , data = ''):
        self.name = name
        self.data = data
        return
    def load(self, connection):
        print "\nLOAD FILE"
        print "%s:\t%s" % (self.name , self.data)
        connection.send(self.data)
        connection.close()
        return

 

def main():
    HOST = ''
    PORT = 50002
    sentinel = False
    found_file = False
    
    opts_list = ["SAVE" , "LOAD"]
    obj_list = []


    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    
    while(sentinel != True):
        s.listen(1)
        connection, address = s.accept()
        mode = connection.recv(4)
        
        if mode == opts_list[0]:#SAVE
            obj = datasave(connection.recv(5),connection.recv(1024))
            connection.close()
            obj_list.append(obj)
            
        elif mode == opts_list[1]:#LOAD
            name = connection.recv(5)
            for obj in obj_list:
                if obj.name == name:
                    found_file = True
                    obj.load(connection)
                    
            if found_file == False:
                connection.send("File Not Found")
            else:
                found_file = False #Always reset sentinels

        else:
            print mode
            sentinel = True
            
    s.close()

main()
