from user import UserConfig


class UserInteract:
    def __init__(self):
        self.channel_name = None
        self.nickname = None
        self.config = None

    def input_config(self, config):
        self.config = config

    def change_nick(self):
        self.nickname = input("Input new nickname:\n")

    def change_channel(self):
        self.channel_name = input("Input new Channel name:\n")

    def output(self):
        print(f"Ip: {self.config.ip} \nPort: {self.config.port}")
        print(f"Username: {self.config.username} \nPassword: {self.config.password}")
