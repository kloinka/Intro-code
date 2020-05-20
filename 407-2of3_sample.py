# This script will create a text browser and display the 'www.tafensw.edu.au' website 

# Author: Eric 

# Date created: 20/05/2020 

import socket 

# Set up a TCP/IP socket 

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

# Connect as client to a selected server 

# on a specified port 

s.connect(("google.com",80)) 

# Protocol exchange - sends and receives 

s.send("GET /robots.txt HTTP/1.0\n\n".encode('utf-8')) 

while True: 

        resp = s.recv(1024).decode()

        if resp == "": break 

        print (resp,) 

# Close the connection when completed 

s.close() 

print ("\ndone" )
