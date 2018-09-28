import socket
import os

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

host = socket.gethostbyname(socket.gethostname())

port = 12345 #server descriptive

server.bind((host,port))
print("Server is ready to listen at {}:{}".format(host,port))
server.listen(5)

print("Server is listing for clints \n\n")

client,client_addr = server.accept()

print(" Connection established with client {}:{}".format(*client_addr))
os.system('cls')
print('\n\n\n')


while True :
    smsg = input('server --> ')
    client.send(smsg.encode())
    cmsg =  client.recv(1024).decode()
    m = 'client --> '+cmsg
    l = len(cmsg)
    print(m.rjust(2*1))
    
    if cmsg == 'bye' or smsg == 'bye' :
        client.close()
        server.close()
        break
