import socket



def main():
    HOST  = ''
    PORT  = 50001    
    message_list = ['alpha' , 'bravo' , 'charlie' , 'delta']
    
    for i in message_list:
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        s.bind((HOST , PORT))
        s.listen(1)
        conn, addr = s.accept()
        conn.send(i)
        conn.close()
        
main()
