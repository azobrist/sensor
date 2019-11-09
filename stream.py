#!/usr/bin/python3
from socket import *

class sio:
    def __init__(self, type="server", buf=1024):
        self.IP = gethostname()
        self.PORT = 5005
        self.BUF = buf
        self.s = socket(AF_INET, SOCK_STREAM)
        self.type = type
        if type == "server":
            try:
                self.s.bind((self.IP, self.PORT))
            except:
                print("address in use")
            self.s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            self.s.listen(1)
            self.conn, self.addr = self.s.accept()
        elif type == "client":
            self.s.connect((self.IP, self.PORT))

    def output(self,msg):
        if self.type == "client":
            self.s.send(bytes(msg,"utf-8"))
            data = self.s.recv(self.BUF)
            return data.decode("utf-8")

    def input(self):
        if self.type == "server":
            data = self.conn.recv(self.BUF)
            self.conn.send(bytes("OK","utf-8"))
            return data.decode("utf-8")

    def __enter__(self):
        self._close()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._close()
        return self

    def _close(self):
        if self.type == "server":
            self.conn.close()
        else:
            self.s.close()

if __name__ == "__main__":
    client = sio("client")
    msg = "Hello"
    print(client.output(msg))


    

