import socket
import threading

def handle_connection(conn, addr):
    print(f'Connected by {addr}')

    while True:
        # Receive Data From Client
        data = conn.recv(1024)
        if not data:
            print(f'Connection closed by {addr}')
            break
        
        message = data.decode('utf-8')
        print(f'Received message from client: {message}')
        
        if message.strip().lower() == 'quit':
            print(f'Closing connection with {addr}')
            break
        
        conn.sendall(data)

    conn.close()

def start_server(host='127.0.0.1', port=65432):
    # Create Socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        print(f'Server started, listening on {host}:{port}')
        s.listen()

        while True:
            # Accept Connection
            conn, addr = s.accept()
            client_thread = threading.Thread(target=handle_connection, args=(conn, addr))  
            client_thread.start()

if __name__ == "__main__":
    start_server()
