'''
Chris Holland
'''
# TCP client from handout

import socket
import sys

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
	print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' +msg[1]
	sys.exit()

print 'Socket created'

host = ''
port = 5000

try:
	remote_ip = socket.gethostbyname(host)
except socket.gaierror:
	print 'Hostname could not be resolved. Exiting.'
	sys.exit()

s.connect((remote_ip, port))
print 'Socket connected to ' + host + ' on ip ' + remote_ip
message = "GET / HTTP/1.1\r\n\r\n"

try:
	s.sendall(message)
except socket.error:
	print 'Send failed'
	sys.exit()

print 'Message sent successfully'
reply = s.recv(4096)
print reply 
s.close()
