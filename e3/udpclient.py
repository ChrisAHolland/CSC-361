'''
Chris Holland
'''
# UDP client taken from handout

import socket
import sys

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socet.error:
	print 'Failed to create socket'
	sys.exit()

host = 'localhost'
port = 8888

while(1):
	msg = raw_input('Enter message to send: ')

	try: 
		s.sendto(msg, (host, port))
		d = s.recvfrom(1024)
		reply = d[0]
		addr = d[1]

		print 'Server reply : ' + reply

	except socket.error, msg:
		print 'Error Code : ' + str(msg[0]) + ' Message' + msg[1]
		sys.exit()

s.close()
