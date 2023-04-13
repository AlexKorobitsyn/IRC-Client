import socket


class ServerInteract:
    def __init__(self, config):
        self.sock = None
        self.config = config

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.config.ip, self.config.port))

    def send_to_server(self, cmd, msg):
        command = "{} {}\r\n".format(cmd, msg)
        self.sock.sendall(command)

    def join_channel(self):
        command = "JOIN"
        channel = self.config.channel
        self.send_to_server(command, channel)

    def set_password(self):
        command = "PASS"
        self.send_to_server(command, self.config.password)

    def set_nickname(self, nickname):
        command = "NICK"
        self.send_to_server(command, nickname)

    def set_username(self):
        command = "USER"
        self.send_to_server(command, self.config.username)

    def get_response(self):
        return self.sock.recv(512)


