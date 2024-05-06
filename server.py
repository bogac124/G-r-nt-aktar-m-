import socket
import cv2
import pickle
import struct

def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "0.0.0.0"  # Tüm ağ arayüzleri üzerinden dinle
    port = 53053

    server.bind((server_ip, port))

    server.listen(6)
    print(f"Listening on {server_ip}:{port}")

    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
    
    cap = cv2.VideoCapture(0)  # Kamera bağlantısını oluştur
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
    
    while True:
        # Alınan verinin boyutunu al
        data_size = client_socket.recv(struct.calcsize("L"))
        if data_size:
            # Veriyi al
            data_size = struct.unpack("L", data_size)[0]
            data = b""
            while len(data) < data_size:
                packet = client_socket.recv(data_size - len(data))
                if not packet:
                    break
                data += packet
            
            # Veriyi işlemeden önce çözümleimport socket
import cv2
import pickle
import struct
import threading

def handle_client(client_socket, client_address):
    print(f"Connection from {client_address} has been established.")

    try:
        while True:
            # İstemciden veri al
            message_size = client_socket.recv(struct.calcsize("L"))
            if not message_size:
                break
            message_size = struct.unpack("L", message_size)[0]
            data = b""
            while len(data) < message_size:
                packet = client_socket.recv(message_size - len(data))
                if not packet:
                    break
                data += packet

            # Alınan veriyi işle
            received_frame = pickle.loads(data)

            # Görüntüyü işle (örneğin, ters çevir)
            processed_frame = cv2.flip(received_frame, 1)

            # İşlenen veriyi istemciye gönder
            data_to_send = pickle.dumps(processed_frame)
            message_size = struct.pack("L", len(data_to_send))
            client_socket.sendall(message_size + data_to_send)

    except Exception as e:
        print(f"Error handling client {client_address}: {e}")

    finally:
        client_socket.close()
        print(f"Connection from {client_address} has been closed.")

def run_server():
    host = "0.0.0.0"  # Tüm arayüzlerden bağlantıları dinle
    port = 53053

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print(f"Server listening on {host}:{port}")

    try:
        while True:
            client_socket, client_address = server.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()
    except KeyboardInterrupt:
        print("Server shutting down...")
        server.close()

# Sunucuyu başlat
run_server()