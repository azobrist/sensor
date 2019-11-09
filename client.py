#!/usr/bin/python2
from tcpcom2 import TCPClient
import time

IP_ADDRESS = "192.168.1.206"
IP_PORT = 22000

ts=0
last=0

def onStateChanged(state, msg):
    global ts
    global last
    global isConnected
    if state == "CONNECTING":
       print("Client:-- Waiting for connection...")
    elif state == "CONNECTED":
       print("Client:-- Connection estabished.")
    elif state == "DISCONNECTED":
       print("Client:-- Connection lost.")
       isConnected = False
    elif state == "MESSAGE":
       print("Client:-- Received data:",msg)
       data = msg.split(",")
    #    print(data)
       ts = float(data[-1])
       print("deltat:",ts-last)
       last=ts

client = TCPClient(IP_ADDRESS, IP_PORT, stateChanged = onStateChanged, isVerbose = False)
rc = client.connect()
msg="go"
cnt = 0
delay_s = 0.1
if rc:
    isConnected = True
    while isConnected:
        print("Client:-- Sending command: go...")
        client.sendMessage(msg)
        time.sleep(delay_s)
        if cnt == 10:
            msg="end"
        cnt+=1
    print("Done")    
else:
    print("Client:-- Connection failed") 
