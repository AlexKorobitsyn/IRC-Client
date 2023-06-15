import os
import threading

from server.AbstractSpeaker import AbstractSpeaker
from server.ServerCommunicator import ServerCommunicator
from ui.UserInterface import UserInterface
from playsound import playsound

from ui.UserInterface import UserInterface
from playsound import playsound


class CUI(UserInterface):

    def __init__(self, speaker: AbstractSpeaker):
        super().__init__(speaker)

    def start(self):
        self.start_input_thread()
        self.start_output_thread()

    def display_input(self):
        while True:
            cmd = input()
            self.speaker.commands_to_server(cmd)

    def display_output(self):
        while self.speaker.signal:
            if self.speaker.logger.data_from_history != "":
                print(self.speaker.logger.data_from_history)
                self.speaker.logger.data_from_history = ""
                self.speaker.user_interact.had_history_to_load = False
            flag = True
            while flag:
                try:
                    data = self.speaker.get_server_response()
                    playsound(os.path.join('audio', 'msg.wav'), block=False)
                    self.speaker.logger.save(data)
                    print(data)
                except TimeoutError:
                    flag = False
                except OSError:
                    flag = False
                except UnicodeDecodeError:
                    print("UnicodeError")

    def input_channel_info(self):
        self.speaker.user_interact.channel_name = input("Input Channel name:\n")
        self.speaker.user_interact.nickname = input("Input nickname:\n")

    def start_input_thread(self):
        input_thread = threading.Thread(target=self.display_input)
        input_thread.start()

    def start_output_thread(self):
        receive_thread = threading.Thread(target=self.display_output, daemon=True)
        receive_thread.start()
