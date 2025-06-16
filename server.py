# server.py
import socket

HOST = '127.0.0.1'  # localhost
PORT = 65432        # Non-privileged port > 1023

try:
    # Create socket object using IPv4 and TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"[SERVER] Listening on {HOST}:{PORT}...")

        # Accept a connection
        conn, addr = server_socket.accept()
        with conn:
            print(f"[SERVER] Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"[SERVER] Received: {data.decode()}")
                conn.sendall(b"Message received!")  # send a response
except Exception as e:
    print(f"[SERVER ERROR] {e}")
