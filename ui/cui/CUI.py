import os

from ui.UserInterface import UserInterface
from playsound import playsound

class CUI(UserInterface):
    def __init__(self, server_communicator):
        super().__init__(server_communicator)

    def display_input(self):
        while True:
            cmd = input()
            self.server_communicator.commands_to_server(cmd)

    def display_output(self):
        while self.server_communicator.signal:
            if self.server_communicator.logger.data_from_history != "":
                print(self.server_communicator.logger.data_from_history)
                self.server_communicator.logger.data_from_history = ""
                self.server_communicator.user_interact.had_history_to_load = False
            flag = True
            while flag:
                try:
                    data = self.server_communicator.serv_interact.get_response().decode('cp1251')
                    playsound(os.path.join('audio', 'msg.wav'), block=False)
                    self.server_communicator.logger.save(data)
                    print(data)
                    if "PING" in data:
                        self.server_communicator.serv_interact.send_to_server("PONG", ":" + data.split(":")[1])
                except TimeoutError:
                    flag = False
                except OSError:
                    flag = False
                except UnicodeDecodeError:
                    print("UnicodeError")
