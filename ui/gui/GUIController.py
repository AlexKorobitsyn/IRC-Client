from ui.apps.PopupMsgCreator import PopupMsgCreator
from ui.apps.StartApp import StartApp
import customtkinter as ctk


class GUIController:
    def __init__(self):
        self.root = ctk.CTk()
        self.start_app = StartApp(self.root)
        self.main_app = None
        self.popup_msg_creator = PopupMsgCreator()
