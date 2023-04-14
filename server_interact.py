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
        command = "{} {}\r\n".format(cmd, msg).encode()
        self.sock.sendall(command)

    def write_private_msg(self):
        msg = input("Write your message:")
        address = input("Message for Who?:")
        command = "PRIVMSG " + address + " :"
        self.send_to_server(command, msg)

    def join_channel(self, channel):
        command = "JOIN"
        self.send_to_server(command, channel)

    def quit(self):
        self.send_to_server("QUIT", "Good bye!")
        print("Quitting ...")

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
        return self.sock.recv(512)
