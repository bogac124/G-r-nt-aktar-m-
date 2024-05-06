import socket
import cv2
import pickle
import struct

def run_client():
    server_ip = "192.168.2.88"  # Sunucu IP adresi
    port = 53053  # Sunucu port numarası

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, port))

    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)  # Kamera bağlantısını oluştur

    while True:
        # Kameradan görüntü al
        ret, frame = cap.read()
        cv2.imshow('sen', frame)
        if ret:
            # Görüntüyü paketleyerek sunucuya gönder
            data = pickle.dumps(frame)
            # Veri boyutunu göndermeden önce bir işaretçi ekleyin
            message_size = struct.pack("L", len(data))
            client_socket.sendall(message_size + data)

        # Sunucudan gelen veriyi al
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
            
            # Veriyi işle
            received_frame = pickle.loads(data)
            
            # Görüntüyü göster
            cv2.imshow('Received', received_frame)

        # Çıkış tuşuna basılınca döngüden çık
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Kapat
    cap.release()
    client_socket.close()
    cv2.destroyAllWindows()

# İstemciyi çalıştır
run_client()