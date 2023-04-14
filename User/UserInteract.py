from User import UserConfig


class UserInteract:
    def __init__(self):
        self.channel_name = None
        self.nickname = None
        self.config = None

    def input_config(self):
        ip, port = input("Input Server Ip and Port:\n").split(" ")
        username, password = input("Input Username and Password:\n").split(" ")
        # Сделать так чтобы username мог содержать пробелы
        config = UserConfig.UserConfig(ip, port, username, password)
        self.config = config

    def input_channel_info(self):
        self.channel_name = input("Input Channel name:\n")
        self.nickname = input("Input nickname:\n")

    def change_nick(self):
        self.nickname = input("Input new nickname:\n")

    def change_channel(self):
        self.channel_name = input("Input new Channel name:\n")

    def output(self):
        print(f"Ip: {self.config.ip} \nPort: {self.config.port}")
        print(f"Username: {self.config.username} \nPassword: {self.config.password}")
