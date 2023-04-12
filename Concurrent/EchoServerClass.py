from asyncio.windows_events import NULL
from http import server
from socket import *
import threading
import time

class EchoServer():
    def __init__(self, host, port):
        self.ServerPort=port
        self.ServerHost=host
        self.ServerSocket = NULL
        self.Conn=NULL
        self.Adrr=NULL
        

    def Start(self):
        counter = 0
        with  socket(AF_INET, SOCK_STREAM) as self.ServerSocket: # IPV4 socket of TCP stream
             self.ServerSocket.bind((self.ServerHost, self.ServerPort))
             self.ServerSocket.listen(5)
             print("Server is ready")
             print(f'listening {(self.ServerHost, self.ServerPort)}')
             while True:
                self.Conn, self.Adrr = self.ServerSocket.accept()
                x=threading.Thread(target=self.ListenToClient)
                x.start()
               
              

    def ListenToClient(self):
        with self.Conn:
                print(f"Connected by {self.Adrr}")
                while True:
                    data = self.Conn.recv(1024)
                    if not data:
                        break
                    self.Conn.sendall(data.upper())


        

