import socket


# 서버 주소
HOST = '127.0.0.1'
# 서버에서 지정해 놓은 포트
PORT = 9999

# 소켓 객체를 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버 접속
client_socket.connect((HOST, PORT))


# 메시지 전송
client_socket.sendall('안녕'.encode())

# 메시지 수신
data = client_socket.recv(1024)
print('Received', repr(data.decode()))

# 소켓 종료
client_socket.close()