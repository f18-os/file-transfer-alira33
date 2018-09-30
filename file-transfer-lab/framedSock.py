import re


def framedSend(sock, payload, debug=0):
    if debug:
        print("framedSend: sending %d byte message" % len(payload))
    msg = str(len(payload)).encode() + b':' + payload
    while len(msg):
        nsent = sock.send(msg)
        msg = msg[nsent:]


rbuf = b""                      # static receive buffer


def framedReceive(sock, debug=0):
    if sock is None:
        print("none")
        return "none"
    global rbuf
    state = "getLength"
    msgLength = -1
    while True:
         r = sock.recv(100)
         print("bye before rec")
         rbuf += r
         if len(r) == 0:
             if len(rbuf) != 0:
                 print("FramedReceive: incomplete message. \n  state=%s, length=%d, rbuf=%s" % (state, msgLength, rbuf))
             return None
         if debug: print("FramedReceive: state=%s, length=%d, rbuf=%s" % (state, msgLength, rbuf))
