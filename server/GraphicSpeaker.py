import os
import sys
import time

from playsound import playsound
from server.AbstractSpeaker import AbstractSpeaker
import customtkinter as ctk

from ui.apps.HelpApp import HelpApp
from ui.apps.QuestionApp import QuestionApp


class GraphicSpeaker(AbstractSpeaker):

    def __init__(self, serv_interact, user_interact):
        super().__init__(serv_interact, user_interact)

    def help_action(self, text):
        root = ctk.CTk()
        root.withdraw()
        help_app = HelpApp(root, text)
        help_app.wait_window()

    def names_action(self):
        channel = self.get_input("Enter channel name:")
        self.serv_interact.take_names_in_channel(channel)

    def privmsg_action(self):
        address = self.get_input("Message for Who?:")
        msg = self.get_input("Write your message:")
        self.serv_interact.write_private_msg(address, msg)

    def quit_action(self):
        playsound(os.path.join('audio', 'end.wav'), block=False)
        self.serv_interact.quit()
        self.serv_interact.sock.close()
        self.signal = False
        exit(0)

    def write_action(self):
        command = self.get_input("Write command:")
        arg = self.get_input("Write argument:")
        self.serv_interact.send_to_server(command, arg)

    def chngnick_action(self):
        nickname = self.get_input("Input new Nickname:")
        self.user_interact.change_nick(nickname)
        self.serv_interact.set_nickname(self.user_interact.nickname)

    def chngchannel_action(self):
        channel = self.get_input("Input new Channel name:")
        self.user_interact.change_channel(channel)
        self.serv_interact.join_channel(self.user_interact.channel_name)

    @staticmethod
    def get_input(prompt):
        root = ctk.CTk()
        root.withdraw()
        question = QuestionApp(root, prompt)
        root.wait_window(question)
        return question.get_answer()
