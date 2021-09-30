from socket import *
serverPort = 12000
BUFSIZ = 1024

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(3)
print ('The server is ready to receive')
while 1:
    connectionSocket, addr = serverSocket.accept()
    print('connected from: ', addr)
    sentence = connectionSocket.recv(BUFSIZ).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
