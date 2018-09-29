#! /usr/bin/env python3

# Echo client program
import socket, sys, re
sys.path.append("../lib")       # for params
import params

switchesVarDefaults = (
    (('-s', '--server'), 'server', "127.0.0.1:50002"),
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )


progname = "fileClient"
paramMap = params.parseParams(switchesVarDefaults)

server, usage  = paramMap["server"], paramMap["usage"]

if usage:
    params.usage()

try:
    serverHost, serverPort = re.split(":", server)
    serverPort = int(serverPort)
except:
    print("Can't parse server:port from '%s'" % server)
    sys.exit(1)

s = None
for res in socket.getaddrinfo(serverHost, serverPort, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        print("creating sock: af=%d, type=%d, proto=%d" % (af, socktype, proto))
        s = socket.socket(af, socktype, proto)
    except socket.error as msg:
        print(" error: %s" % msg)
        s = None
        continue
    try:
        print(" attempting to connect to %s" % repr(sa))
        s.connect(sa)
    except socket.error as msg:
        print(" error: %s" % msg)
        s.close()
        s = None
        continue
    break

if s is None:
    print('could not open socket')
    sys.exit(1)

file = open ("input.txt", "rb")
lines = file.read(1024)


s.shutdown(socket.SHUT_WR)      # no more output

while (lines):
    print(lines)
    s.send(lines)
    print("Received '%s'" % lines)
    if len(lines) == 0:
        break
print("Zero length read.  Closing")
s.close()