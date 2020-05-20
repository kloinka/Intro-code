# This script will create a text browser and display the 'www.tafensw.edu.au' website 

# Author: Eric 

# Date created: 20/05/2020 

import socket
import ssl
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
addr = ('tafensw.edu.au', 443)
ss.connect(addr)
ss.send('GET / HTTP/1.0\n\n'.encode('utf-8'))
while True: 
        resp = ss.recv(1024).decode()
        if resp == "": break 
        print (resp)
ss.close()
