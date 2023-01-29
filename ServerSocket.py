import socket


def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5004  # initiate port no above 1024

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind(('192.168.0.108', port))  # bind host address and port together
    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept d
        # ata packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break

        print("from connected user: " + str(data))
        data = f'User {str(address)} you have a removable devices connected to you system, be mindful of virus'
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


server_program()
