#!/usr/bin/python2
from tcpcom2 import TCPServer
import time

IP_PORT = 22000

def onStateChanged(state, msg):
    print(state)
    if state == "LISTENING":
        print("Server:-- Listening...")
    elif state == "CONNECTED":
        print("Server:-- Connected to {0}".format(msg))
    elif state == "MESSAGE":
        print("Server:-- Message received: {0}".format(msg))
        if msg == "go":
            server.sendMessage("Hello")

server = TCPServer(IP_PORT, stateChanged = onStateChanged)