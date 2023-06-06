from server.ServerCommunicator import ServerCommunicator
from ui.UserInterface import UserInterface


class CUI(UserInterface):

    def __init__(self, server_communicator: ServerCommunicator):
        super().__init__(server_communicator)

    def display_input(self):
        while True:
            cmd = input()
            self.server_communicator.commands_to_server(cmd)

    def display_output(self):
        while self.server_communicator.signal:
            flag = True
            while flag:
                try:
                    data = self.server_communicator.get_server_response()
                    print(data)
                except TimeoutError:
                    flag = False
                except OSError:
                    flag = False
                except UnicodeDecodeError:
                    print("UnicodeError")

    def input_channel_info(self):
        self.server_communicator.user_interact.channel_name = input("Input Channel name:\n")
        self.server_communicator.user_interact.nickname = input("Input nickname:\n")
