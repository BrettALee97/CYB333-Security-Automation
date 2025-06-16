# client.py
import socket

HOST = '127.0.0.1'  # Server IP
PORT = 65432        # Same port as server

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print(f"[CLIENT] Connected to server at {HOST}:{PORT}")
        
        # Send a message
        message = "Hello from client!"
        client_socket.sendall(message.encode())
        
        # Wait for a response
        response = client_socket.recv(1024)
        print(f"[CLIENT] Server responded: {response.decode()}")

except ConnectionRefusedError:
    print("[CLIENT ERROR] Could not connect to server – is it running?")
except Exception as e:
    print(f"[CLIENT ERROR] {e}")