import socket
import threading
from sys import argv

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        message = data.decode("utf-8")
        print(f"Received message from {addr}: {message}")
        
        conn.sendall(f"Echo: {message}".encode("utf-8"))
        
        if message.strip().lower() == "end":
            print(f"Ending connection with {addr}")
            break

    conn.close()
    print(f"Connection closed with {addr}")

def main():
    try:
        port = int(argv[1])
    except:
        port = 8080

    print(f"Server started on port {port}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("0.0.0.0", port))
        s.listen(5)  
        print("Waiting for clients...")

        while True:
            conn, addr = s.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()

if __name__ == "__main__":
    main()
