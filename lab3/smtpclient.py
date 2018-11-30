'''
Chris Holland
V00876844
'''

from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "smtp.uvic.ca"
port = 25

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
    
# Send MAIL FROM command and print server response.
print "Send Email from..."
sender = raw_input()
MAILFROM = "MAIL FROM: <" + sender + ">\r\n"
clientSocket.send(MAILFROM.encode()) 
recv2 = clientSocket.recv(1024).decode()
print recv2

# Send RCPT TO command and print server response. 
print "Send Email to..."
receiver = raw_input()
RCPTO = "RCPT TO: <" + receiver + ">\r\n"
clientSocket.send(RCPTO.encode())
recv3 = clientSocket.recv(1024).decode()
print recv3

# Send DATA command and print server response. 
DATA = "DATA\r\n"
clientSocket.send(DATA.encode())
recv4 = clientSocket.recv(1024).decode()
print recv4

# Send message data
clientSocket.send(msg.encode())

# Message ends with a single period.
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
print recv5.decode()
# Send QUIT command and get server response.
QUIT = "QUIT\r\n"
clientSocket.send(QUIT.encode())

recv6 = clientSocket.recv(1024).decode()
print recv6

clientSocket.close()
