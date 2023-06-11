from server.AbstractSpeaker import AbstractSpeaker
from ui.UserInterface import UserInterface
from ui.apps.ChannelInfoApp import ChannelInfoApp
from ui.gui.GUIController import GUIController
from ui.apps.InputApp import InputApp
import customtkinter as ctk

from ui.apps.OutputApp import OutputApp


class GUI(UserInterface):

    def __init__(self, speaker: AbstractSpeaker, gui_controller: GUIController):
        super().__init__(speaker)
        self.gui_controller = gui_controller

    def display_input(self):
        input_app = InputApp(ctk.CTk(), self.speaker)
        input_app.wait_window()

    def display_output(self):
        output_app = OutputApp(ctk.CTk(), self.speaker)
        output_app.wait_window()

    def input_channel_info(self):
        channel_info_app = ChannelInfoApp(self.speaker)
        channel_info_app.wait_window()
