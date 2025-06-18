import socket
import ssl
import threading

# Thông tin server
server_address = ('localhost', 12345)

# Hàm để nhận dữ liệu từ server
def receive_data(ssl_socket):
    try:
        while True:
            data = ssl_socket.recv(1024)
            if not data:
                break
            print("Nhận:", data.decode('utf-8'))
    except:
        # Lỗi xảy ra khi server đóng kết nối hoặc có vấn đề khác
        pass
    finally:
        # Đóng socket khi luồng nhận kết thúc
        ssl_socket.close()
        print("Kết nối đã đóng.")

# --- Phần chính của client ---

# Tạo socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tạo SSL context
# Cấu hình này bỏ qua việc xác minh chứng chỉ, chỉ dùng cho mục đích phát triển
context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.verify_mode = ssl.CERT_NONE 
context.check_hostname = False

# Bọc socket trong SSL và kết nối đến server
ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')
ssl_socket.connect(server_address)

# Bắt đầu một luồng (thread) riêng để lắng nghe dữ liệu từ server
receive_thread = threading.Thread(target=receive_data, args=(ssl_socket,))
receive_thread.start()

# Luồng chính để gửi dữ liệu đi
try:
    # Vòng lặp vô hạn để người dùng nhập và gửi tin nhắn
    while True:
        message = input("Nhập tin nhắn: ")
        ssl_socket.send(message.encode('utf-8'))
except KeyboardInterrupt:
    # Người dùng nhấn Ctrl+C để thoát
    print("\nĐang đóng kết nối...")
except Exception as e:
    # Bắt các lỗi khác có thể xảy ra khi gửi tin
    print(f"Lỗi khi gửi dữ liệu: {e}")
finally:
    # Đảm bảo socket được đóng khi vòng lặp kết thúc
    ssl_socket.close()