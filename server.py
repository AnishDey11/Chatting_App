import socket
import threading
from ipid import server_local, server_public


PORT = 5050
# SERVER = socket.gethostbyname(socket.gethostname())
# SERVER = '127.0.0.1' #Random
SERVER = server_local
# SERVER = server_public #This is to connect overall
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!Disconnect'
clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def broadcast(message, current_client, current_addr, all_clients):
    for client in all_clients:
        if client != current_client:
            total = f"{current_addr}: " + message
            client.send(total.encode(FORMAT))

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    while connected:
        msg = conn.recv(2048).decode(FORMAT)
        if msg:
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            broadcast(msg, conn, addr, clients)
            # print(clients)
            # for client in clients:
            #     if client[1] == addr[1]:
            #         continue
            #     else:
                    # conn.send(f"Message Received".encode(FORMAT))
                    # conn.send(f"{msg}".encode(FORMAT))
            # conn.send(f"{msg}".encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")

print("[STARTING] server is starting......")
start()
