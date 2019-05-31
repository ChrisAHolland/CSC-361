'''
Chris Holland
CSC 361, Lab 1
server.py
'''

from socket import *
import sys

host = ''
port = 6789

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind((host, port))

serverSocket.listen(10)

while 1:
	print 'Ready to serve...'
	connectionSocket, addr = serverSocket.accept()

	try:
		message = connectionSocket.recv(1024)
		filename = message.split()[1]
		f = open(filename[1:])

		outputdata = f.read()
		connectionSocket.send('HTTP/1.1 200 OK\n' + 'Content-Type: text/html\n' + '\r\n')

		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode())
		
		connectionSocket.send("\r\n".encode())
 		connectionSocket.close()
		
	except IOError:
		connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n')
		connectionSocket.send('<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n')
		connectionSocket.close()

serverSocket.close()
sys.exit()
