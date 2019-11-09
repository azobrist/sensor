#!/usr/bin/python3
from tcpcom import TCPServer
from socket import *

import time

print(gethostname())
IP_PORT = 22000

def onStateChanged(state, msg):
    if state == "LISTENING":
        print( "Server:-- Listening...")
    elif state == "CONNECTED":
        print(f"Server:-- Connected to{msg}")
    elif state == "MESSAGE":
        print(f"Server:-- Message received:{msg}")
        if msg == "go":
            server.sendMessage("Hello")

server = TCPServer(IP_PORT, stateChanged = onStateChanged)