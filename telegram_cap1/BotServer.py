import socket

class BotServer:
    def __init__(self, srv_port, listen_num):
        self.port=srv_port # 소켓 서버의 포트번호
        self.listen=listen_num #동시 접속 클라이언트 수
        self.mySock = None

    #sock 생성, TCP/IP 소켓 생성 및 서버 포트로 지정한 서버 포트로 설정한 수 만큼 클라이언트 연결 수락
    def create_sock(self):
        self.mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #소켓 닫아도 바로 사용가능하게 설정
        self.mySock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.mySock.bind(("0.0.0.0", int(self.port)))
        self.mySock.listen(int(self.listen))
        return self.mySock

    #client 대기 챗봇 클라이언트 연결을 대기하다 연결을 수락
    def ready_for_client(self):
        return self.mySock.accept()

    #현재 생성된 서버 소켓을 반환
    def get_sock(self):
        return self.mySock