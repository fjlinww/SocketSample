from socket import *
serverName = '127.0.0.1'
serverPort = 12000
BUFSIZ = 2048

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(),(serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(BUFSIZ)
modifiedMessage = modifiedMessage.decode()
print(modifiedMessage)

clientSocket.close()
