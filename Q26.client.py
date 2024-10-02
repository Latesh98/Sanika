import socket

def send_string_to_server(input_string):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 65432))

    client_socket.sendall(input_string.encode('utf-8'))
    modified_string = client_socket.recv(1024).decode('utf-8')

    print(f"Modified string received from server: {modified_string}")
    client_socket.close()

# Example usage
if __name__ == "__main__":
    input_string = "Hello World"
    send_string_to_server(input_string)
