import socket
import threading

def handle_client(conn, address):
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))
        response = f'User {str(address)}, you have a removable device connected to your system. Be mindful of viruses.'
        conn.send(response.encode())
    conn.close()

def server_program():
    host = socket.gethostname()
    port = 5004

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.0.108', port))
    server_socket.listen(2)

    while True:
        conn, address = server_socket.accept()
        print("Accepted connection from {}".format(address))
        client_thread = threading.Thread(target=handle_client, args=(conn, address))
        client_thread.start()

server_program()
