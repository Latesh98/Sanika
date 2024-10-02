import socket

def replace_non_vowels(input_string):
    vowels = "aeiouAEIOU"
    return ''.join(char if char in vowels else '$' for char in input_string)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen(1)
    print("Server is listening for connections...")

    conn, addr = server_socket.accept()
    print(f"Connection from {addr} has been established!")

    data = conn.recv(1024).decode('utf-8')
    print(f"Received string: {data}")

    modified_string = replace_non_vowels(data)
    conn.sendall(modified_string.encode('utf-8'))
    print(f"Modified string sent: {modified_string}")

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
