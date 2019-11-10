#!/usr/bin/python2
from tcpcom2 import TCPServer
from read import *
import time

IP_PORT = 22000

def onStateChanged(state, msg):
    if state == "LISTENING":
        print("Server:-- Listening...")
    elif state == "CONNECTED":
        print("Server:-- Connected to", msg)
    elif state == "MESSAGE":
        print("Server:-- Message received:",msg)
        # p = msg.split(",")
        # cmd = p[0]
        # delay = p[1]
        if msg == "go":
            server.setTimeout(5)
            msg = read_all(imu)
            server.sendMessage(msg)
        if msg == "end":
            server.terminate()

server = TCPServer(IP_PORT, stateChanged = onStateChanged, isVerbose = False)