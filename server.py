#!/usr/bin/python3
from tcpcom import TCPServer
import time

IP_PORT = 22000

def onStateChanged(state, byt):
    print(state)
    msg = byt.decode()
    if state == "LISTENING":
        print("Server:-- Listening...")
    elif state == "CONNECTED":
        print("Server:-- Connected to {0}".format(msg))
    elif state == "MESSAGE":
        print("Server:-- Message received: {0}".format(msg))
        if msg == "go":
            server.sendMessage("Hello")
        if msg == "end":
            server.terminate()

server = TCPServer(IP_PORT, stateChanged = onStateChanged, isVerbose = True)