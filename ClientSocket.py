import socket
import time
import psutil


def detector():
    require_devices = []
    devices_connected = psutil.disk_partitions(True)
    for device in devices_connected:
        if "C:\\" not in device.mountpoint:
            require_devices.append(device)
    time.sleep(30)
    return require_devices


def detect_device():
    while True:
        devices = detector()
        if len(devices) > 0:
            return devices


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    # take input
    message = ""
    # data = detect_device()
    while message.lower().strip() != 'bye':
        received_devices = detect_device()
        for device in received_devices:
            message = f'{device}'
            client_socket.send(message.encode())  # send message
            # client_socket.send(data.encode())  # send
            data = client_socket.recv(1024).decode()  # receive response

            print('Alert  from server: ' + data)  # show in terminal
        #
        # message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


client_program()