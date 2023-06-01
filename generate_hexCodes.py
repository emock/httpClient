#/bin/python3


with open("hexcodes.txt", "ab") as file:
    for i in range(16,256):
        print(hex(i))
        file.write(bytes.fromhex(hex(i)[2:]))
