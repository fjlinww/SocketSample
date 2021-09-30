from socket import *
serverPort = 12000
BUFSIZ = 2048

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print ('The server is ready to receive')
while 1:
    message, clientAddress = serverSocket.recvfrom(BUFSIZ)
    message = message.decode()
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    print('...received from and sent to', clientAddress)
