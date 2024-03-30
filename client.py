import socket

def start_client(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the server
        s.connect((host, port))
        print(f'Connected to server {host}:{port}')

        while True:
            message = input('Enter message (type "quit" to exit): ')
            s.sendall(message.encode('utf-8'))
            
            if message.strip().lower() == 'quit':
                print('Closing connection')
                break
            
            # Message Received By Server
            data = s.recv(1024)
            print(f'Received from server: {data.decode("utf-8")}')

if __name__ == "__main__":
    start_client()
