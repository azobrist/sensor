#!/usr/bin/python2
from tcpcom2 import TCPClient
import time

IP_ADDRESS = "192.168.1.206"
IP_PORT = 22000

def onStateChanged(state, msg):
    print(state)
    global isConnected
    if state == "CONNECTING":
       print("Client:-- Waiting for connection...")
    elif state == "CONNECTED":
       print("Client:-- Connection estabished.")
    elif state == "DISCONNECTED":
       print("Client:-- Connection lost.")
       isConnected = False
    elif state == "MESSAGE":
       print("Client:-- Received data: {0}".format(msg))

client = TCPClient(IP_ADDRESS, IP_PORT, stateChanged = onStateChanged)
rc = client.connect()
msg="go"
if rc:
    isConnected = True
    while isConnected:
        print("Client:-- Sending command: go...")
        client.sendMessage(msg)
        time.sleep(2)
        msg="end"
    print("Done")    
else:
    print("Client:-- Connection failed") 
