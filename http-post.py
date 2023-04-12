import socket


ADDR = "127.0.0.1"
PORT = 9000


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect((ADDR, PORT))

#this is why the send() method wants bytes in input.
# So our text string must be converted to binary first.
# In Python this is done by prepending a b to it:

sock.send(b"POST / HTTP/1.1\r\n\r\n")

response = sock.recv(4096)

print(response)
print(response.decode())
