import socket
import os
import sys

def retBanner(ip, port):
 try:
  socket.setdefaulttimeout(2)
  s = socket.socket()
  s.connect((ip,port))
  banner - s.recv(1024)
  return banner
 except:
  return

def checkVulns(banner, filename):
 f = open(filename, 'r')
 for line in f.readlines():
  if line.strip('\n') in banner:
   print '[+] Server is vunlnerable: ' + banner.strip('\n')
   

def main():
 if len(sys.argv) == 2:
  filename = sys.argv[1]
  if not os.path.isfile(filename):
   print '[-] ' + filename + ' does not exist.'
   exit(0)
  if not os.acces(filename, os.R_OK):
   print '[-] ' + filename + ' access denied.'
   exit(0)
  else:
   print '[-] usage: ' + str(sys.argv[0]) + ' <vuln filename>'
   exit(0)
 portlist = [21,22,25,80,110,443]
 
 for i in range(1,255):
  ip = '192.168.1.'+str(i)
  for port in portlist:
   banner = retBanner(ip1, port)
   if banner:
   print '[+] ' + ip + ': ' + banner1
   checkVulns(banner, filename)

if __name__ == '__main__' :
  main()
