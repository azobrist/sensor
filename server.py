#!/usr/bin/python2
from tcpcom2 import TCPServer
from read import *
import time

IP_PORT = 22000

def onStateChanged(state, msg):
    print(state)
    if state == "LISTENING":
        print("Server:-- Listening...")
    elif state == "CONNECTED":
        print("Server:-- Connected to", msg)
    elif state == "MESSAGE":
        print("Server:-- Message received:",msg)
        if msg == "go":
            server.sendMessage(read_all(imu))
        if msg == "end":
            server.terminate()

server = TCPServer(IP_PORT, stateChanged = onStateChanged, isVerbose = False)