from socket import *

serverHost = '127.0.0.1'
serverPort = 12001

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverHost, serverPort))
sentence = input('input lowercase sentence (q for stop): ')
while(sentence!='q'):
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print('From Server: ', modifiedSentence.decode())
    sentence = input('input lowercase sentence (q for stop): ')
clientSocket.close()