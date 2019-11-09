#!/usr/bin/python3
import socket
from stream import sio

with sio("server") as server:
    print(server.input())

