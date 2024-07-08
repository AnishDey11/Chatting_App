import socket
import threading
from ipid import server_local, server_public

PORT = 5050
SERVER = server_local # Must be equal to serevers one
# SERVER = '127.0.0.1' # Random
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = '!Disconnect'
FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg:str):
    # while True:
        # msg = input("<<< ")
    message = msg.encode(FORMAT)
    client.send(message)
        # print(client.recv(2048).decode(FORMAT))
        # print(client.recv(2048).decode(FORMAT))

def take_msg():
    while True:
        try:
            recv_msg = client.recv(2048).decode(FORMAT)
            if not recv_msg:
                break
            # print(recv_msg)
            return recv_msg
        except:
            break

# send("New")
# input()
# send("Hello Internet")
# input()
# send(DISCONNECT_MESSAGE)
# send(input('<<< '))
# print(client.recv(2048).decode(FORMAT))
# while True:
# thread = threading.Thread(target=send)
# thread_ = threading.Thread(target=take_msg)
# msg = input("<<< ")
# thread.start()

# thread_.start()



