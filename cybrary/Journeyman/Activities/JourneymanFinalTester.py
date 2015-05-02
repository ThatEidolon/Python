import socket

PORT = 50002

files = {
        "File1" : "The quick brown fox jumped over the lazy dogs" ,
        "File2" : "If a woodchuck could chuck wood" ,
        "File3" : "Now you're just showing off" ,
        }


for i in files:
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.connect(('127.0.0.1', PORT))
    s.send("SAVE")
    s.send(i)
    s.send(files[i])
    s.close()

for i in files:
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.connect(('127.0.0.1', PORT))
    s.send("LOAD")
    s.send(i)
    data = s.recv(1024)
    if data != files[i]:
        print "Failed: %s != %s" % (data , files[i])
    s.close()
    
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.connect(('127.0.0.1', PORT))
s.send("LOAD")
s.send("File4")
data = s.recv(1024)
if data != "File Not Found":
    print "Error check failed"
else:
    print "SUCCESS!"
s.close()
