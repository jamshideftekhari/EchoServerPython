# Make a cuncurrent server receiving a text from another processes
from pickle import TRUE
from EchoServerClass import EchoServer
import time

serverPort = 12001         # Port to listen on (non-privileged ports are > 1023)
serverHost = "127.0.0.1"   # standard loop back interface address (localhost)


#while True:
serverObject = EchoServer(serverHost,serverPort)
serverObject.Start()
#x=threading.Thread(target=serverObject.ListenToClient)
#x.start()

#while True:
#    counter = 0
#    print("Waiting for client to connect" + str(counter+1))
#    time.sleep(2) 
