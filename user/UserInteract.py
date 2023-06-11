from user import UserConfig


class UserInteract:
    def __init__(self):
        self.channel_name = None
        self.nickname = None
        self.config = None
        self.had_history_to_load = False

    def input_config(self, config):
        self.config = config

    def change_nick(self, nickname):
        self.nickname = nickname

    def change_channel(self, channel_name):
        self.channel_name = channel_name

    def output(self):
        print(f"Ip: {self.config.ip} \nPort: {self.config.port}")
        print(f"Username: {self.config.username} \nPassword: {self.config.password}")
