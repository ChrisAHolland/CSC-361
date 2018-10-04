'''
Chris Holland
V00876844
csc 361, lab 1
client.py
'''

from socket import *
import sys

s = socket(AF_INET, SOCK_STREAM)

host = str(sys.argv[1])
 
port = int(sys.argv[2])

filename = str(sys.argv[3])

s.connect((host, port))

message = 'GET ' + '/' + filename + ' HTTP/1.1\n\r\n'

s.sendall(message)

reply = s.recv(4096)

print reply
