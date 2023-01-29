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
    print("Server Name: " + host + " running on port: "+str(port))
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    your_local_ip_address = "192.168.0.112"
    server_socket.bind((your_local_ip_address, port))
    number_of_connections = 2
    server_socket.listen(number_of_connections)

    while True:
        conn, address = server_socket.accept()
        print("Accepted connection from {}".format(address))
        client_thread = threading.Thread(target=handle_client, args=(conn, address))
        client_thread.start()


server_program()
