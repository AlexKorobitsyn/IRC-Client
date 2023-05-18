import threading

from server.ServerCommunicator import ServerCommunicator
from ui.cui.CUI import CUI
from ui.gui.GUI import GUI
from ui.gui.GUIController import GUIController
from server.ServerInteract import ServerInteract
from user.UserInteract import UserInteract


class IRCClient:
    def __init__(self):
        self.server_communicator = ServerCommunicator(None, UserInteract())
        self.gui_controller = GUIController()
        self.user_interface = None

    def start_input_thread(self):
        input_thread = threading.Thread(target=self.user_interface.display_input)
        input_thread.start()

    def start_output_thread(self):
        receive_thread = threading.Thread(target=self.user_interface.display_output, daemon=True)
        receive_thread.start()

    def connect(self):
        self.server_communicator.user_interact.input_channel_info()

        self.server_communicator.serv_interact = ServerInteract(self.server_communicator.user_interact.config)
        self.server_communicator.serv_interact.connect()
        self.server_communicator.serv_interact.set_nickname(self.server_communicator.user_interact.nickname)
        self.server_communicator.serv_interact.set_username(self.server_communicator.user_interact.config.username)

    def start_app_iteration(self):
        self.gui_controller.start_app.wait_window()  # Ожидание закрытия окна start_app
        self.server_communicator.user_interact.input_config(self.gui_controller.start_app.user_config)
        self.server_communicator.user_interact.output()

    def choose_interface(self):
        interface = self.gui_controller.popup_msg_creator.create_choice_of_two_options(
            "В каком интерфейсе продолжим?",
            "GUI",
            "CUI"
        )
        match interface:
            case "GUI":
                self.user_interface = GUI(self.server_communicator, self.gui_controller.main_app)
            case "CUI":
                self.user_interface = CUI(self.server_communicator)

    def run(self):
        self.start_app_iteration()
        self.choose_interface()
        self.connect()
        self.start_input_thread()
        self.start_output_thread()


if __name__ == '__main__':
    irc_client = IRCClient()
    irc_client.run()
