from ui.UserInterface import UserInterface


class CUI(UserInterface):
    def __init__(self, server_communicator):
        super().__init__(server_communicator)

    def display_input(self):
        while True:
            cmd = input()
            self.server_communicator.commands_to_server(cmd)

    def display_output(self):
        self.server_communicator.output_from_server()
