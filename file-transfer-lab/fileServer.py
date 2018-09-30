#! /usr/bin/env python3

# Echo server program
import params
import socket, sys, re
sys.path.append("../lib")       # for params
from framedSock import framedSend, framedReceive

switchesVarDefaults = (
    (('-l', '--listenPort') ,'listenPort', 50002),
    (('-d', '--debug'), "debug", False), # boolean (set if present)
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )



progname = "fileserver"
paramMap = params.parseParams(switchesVarDefaults)

debug, listenPort = paramMap['debug'], paramMap['listenPort']

if paramMap['usage']:
    params.usage()

listenPort = paramMap['listenPort']
listenAddr = ''       # Symbolic name meaning all available interfaces

if paramMap['usage']:
    params.usage()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((listenAddr, listenPort))
s.listen(1)              # allow only one outstanding request
# s is a factory for connected sockets

conn, addr = s.accept()  # wait until incoming connection request (and accept it)
print('Connected by', addr)
while True:
    (conn, address) = s.accept()
    text_file = 'output.txt'
 
    #Receive, output and save file
    with open(text_file, "wb") as fw:
        print("Receiving..")
        while True:
            print('receiving')
            data = conn.recv(32)
            if data == b'BEGIN':
                continue
            elif data == b'ENDED':
                print('Breaking from file write')
                break
            else:
                print('Received: ', data.decode('utf-8'))
                fw.write(data)
                print('Wrote to file', data.decode('utf-8'))
        fw.close()
        print("Received..")
 
    #Append and send file
    print('Opening file ', text_file)
    with open(text_file, 'ab+') as fa:
        print('Opened file')
        print("Appending string to file.")
        string = b"Append this to file."
        fa.write(string)
        fa.seek(0, 0)
        print("Sending file.")
        while True:
            data = fa.read(1024)
            conn.send(data)
            if not data:
                break
        fa.close()
        print("Sent file.")
    break
s.close()