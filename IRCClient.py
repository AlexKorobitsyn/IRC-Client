import os
import threading

from server.GraphicSpeaker import GraphicSpeaker
from server.CommandSpeaker import CommandSpeaker
from server.ServerCommunicator import ServerCommunicator
from ui.cui.CUI import CUI
from ui.gui.GUI import GUI
from ui.gui.GUIController import GUIController
from server.ServerInteract import ServerInteract
from user.UserInteract import UserInteract
from playsound import playsound


class IRCClient:
    def __init__(self):
        self.server_communicator = None
        self.gui_controller = GUIController()
        self.user_interface = None

    def connect(self):
        self.user_interface.input_channel_info()
        self.server_communicator.serv_interact.connect()
        self.server_communicator.serv_interact.set_nickname(self.server_communicator.user_interact.nickname)
        self.server_communicator.serv_interact.set_username(self.server_communicator.user_interact.config.username)
        self.server_communicator.serv_interact.join_channel(self.server_communicator.user_interact.channel_name)

    def get_user_config(self):
        playsound(os.path.join('audio', 'start.mp3'), block=False)
        self.gui_controller.start_app.wait_window()  # Ожидание закрытия окна start_app
        user_interact = UserInteract()
        user_interact.input_config(self.gui_controller.start_app.user_config)
        serv_interact = ServerInteract(user_interact.config)

        self.server_communicator = ServerCommunicator(serv_interact, user_interact)

    def choose_interface(self):
        interface = self.gui_controller.popup_msg_creator.create_choice_of_two_options(
            "В каком интерфейсе продолжим?",
            "CUI",
            "GUI"
        )
        match interface:
            case "GUI":
                self.server_communicator.speaker = \
                    GraphicSpeaker(self.server_communicator.serv_interact, self.server_communicator.user_interact)
                self.server_communicator.speaker.make_logger()
                self.user_interface = GUI(self.server_communicator.speaker, self.gui_controller)
            case "CUI":
                self.server_communicator.speaker = \
                    CommandSpeaker(self.server_communicator.serv_interact, self.server_communicator.user_interact)
                self.server_communicator.speaker.make_logger()
                self.user_interface = CUI(self.server_communicator.speaker)

    def run(self):
        self.get_user_config()
        self.choose_interface()
        self.connect()
        self.run_interface()

    def run_interface(self):
        self.user_interface.start()
