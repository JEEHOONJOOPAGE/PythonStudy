import socket


# 접속할 서버 주소(local)
HOST = '127.0.0.1'

# 클라이언트 접속을 대기하는 포트
PORT = 9999



# 소켓 객체를 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#서버소켓 생성
server_socket.bind((HOST, PORT))

# 서버 준비
server_socket.listen()

# accept 함수에서 대기하다가 클라이언트가 접속하면 새로운 소켓을 리턴합니다.
client_socket, addr = server_socket.accept()

# 접속한 클라이언트의 주소입니다.
print('Connected by', addr)
#print('Connected by', client_socket)

while True:

    # 클라이언트가 보낸 메시지를 수신하기 위해 대기
    # 수신 길이 1024로 지정
    data = client_socket.recv(1024)

    # 빈 문자열을 수신하면 종료
    if not data:
        break

    # 수신받은 문자열을 출력
    print('Received from', addr, data.decode())

    # 받은 문자열을 다시 클라이언트로 전송
    client_socket.sendall(data)


# 소켓을 종료
client_socket.close()
server_socket.close()