import socket


class ServerInteract:
    def __init__(self, config):
        self.sock = None
        self.config = config

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.config.ip, self.config.port))
        self.sock.settimeout(0.2)

    def send_to_server(self, cmd, msg=""):
        command = f"{cmd} {msg}\r\n".encode()
        self.sock.sendall(command)

    def take_channel_list(self):
        self.sock.sendall("LIST\r\n".encode())

    def take_names_in_channel(self, channel):
        self.send_to_server("NAMES", channel)

    def write_private_msg(self, address, msg):
        command = "PRIVMSG " + address + " :"
        self.send_to_server(command, msg)

    def join_channel(self, channel):
        command = "JOIN"
        self.send_to_server(command, channel)

    def quit(self):
        self.send_to_server("QUIT", "Good bye!")  # TODO почему одно слово только???

    def set_password(self):
        command = "PASS"
        self.send_to_server(command, self.config.password)

    def set_nickname(self, nickname):
        command = "NICK"
        self.send_to_server(command, nickname)

    def set_username(self, real_name, ip="localhost"):
        command = "USER {} {} {} :{}\r\n".format(self.config.username, ip, "*", real_name).encode()
        self.sock.sendall(command)

    def get_response(self):
        gog = self.sock.recv(1024)
        return gog
