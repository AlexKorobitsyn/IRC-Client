from ui.UserInterface import UserInterface


class GUI(UserInterface):
    def __init__(self, server_communicator, main_app):
        super().__init__(server_communicator)
        self.main_app = main_app

    def display_input(self):
        pass

    def display_output(self):
        pass
