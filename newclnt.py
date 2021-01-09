import socket

Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '10.0.2.16'
port = 8888

print('Waiting for connection')
try:
    Client.connect((host, port))
except socket.error as e:
    print(str(e))

#Response = Client.recv(1024)
#print(Response)
while True:
   # Input = input('Say Something: ')
   # ClientSocket.send(str.encode(Input))
    Response = Client.recv(1024)
    print(Response.decode('utf-8'))

    #name = input("Enter your name: ")
    #ClientSocket.send(str.encode(name))
    #reply = ClientSocket.recv(1024)

    #print("Hi player: " + str(reply.decode('utf-8')))

    try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            name = input('Enter your name: ')
            Client.send(str.encode(name))
            reply = Client.recv(1024)
            #print("Hi player: " + str(reply.decode('utf-8')))


    except:
            # Close Connection When Error
            print("An error occured!")
            Client.close()
            break

Client.close()

