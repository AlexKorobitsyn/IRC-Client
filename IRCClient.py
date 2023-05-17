import threading

from gui.MainApp import MainApp
from gui.StartApp import StartApp
from server.ServerInteract import ServerInteract
from user.UserInteract import UserInteract


class IRCClient:
    def __init__(self):
        self.user_interact = UserInteract()
        self.serv_interact = None
        self.signal = True
        self.start_app = StartApp()

    def commands_to_server(self, cmd):
        match cmd:
            case "NAMES":
                self.serv_interact.take_names_in_channel()
            case "LIST":
                self.serv_interact.take_channel_list()
            case "JOIN":
                self.serv_interact.join_channel(self.user_interact.channel_name)
            case "SS":
                print("Hi")
            case "USER":
                self.serv_interact.set_username(self.user_interact.config.username)
            case "CHNGNICK":
                self.user_interact.change_nick()
                self.serv_interact.set_nickname(self.user_interact.nickname)
            case "CHNGCHANNEL":
                self.user_interact.change_channel()
                self.serv_interact.join_channel(self.user_interact.channel_name)
            case "HELP":
                print("THATS HELP, LOOK IN THE CODE")
            case "PRIVMSG":
                self.serv_interact.write_private_msg()
            case "QUIT":
                self.serv_interact.quit()
                self.serv_interact.sock.close()
                signal = False
            case "WRITE":
                command = input("Write command:")
                arg = input("Write argument:")
                self.serv_interact.send_to_server(command, arg)
            case "":
                print("Print \"HELP\"")

    def receive_from_server(self):
        while self.signal:
            flag = True
            while flag:
                try:
                    data = self.serv_interact.get_response().decode('cp1251')
                    print(data)
                    if "PING" in data:
                        self.serv_interact.send_to_server("PONG", ":" + data.split(":")[1])
                except TimeoutError:
                    flag = False
                except UnicodeDecodeError:
                    print("UnicodeError")

    def input_cycle(self):
        while True:
            cmd = input()
            self.commands_to_server(cmd)

    def start_input_thread(self):
        input_thread = threading.Thread(target=self.input_cycle)
        input_thread.start()

    def start_receive_thread(self):
        receive_thread = threading.Thread(target=self.receive_from_server, daemon=True)
        receive_thread.start()

    def connect(self):
        self.user_interact.input_config(self.start_app.user_config)
        self.user_interact.output()
        self.user_interact.input_channel_info()

        self.serv_interact = ServerInteract(self.user_interact.config)
        self.serv_interact.connect()
        self.serv_interact.set_nickname(self.user_interact.nickname)

    def run(self):
        self.start_app.mainloop()
        self.connect()
        self.start_input_thread()
        self.start_receive_thread()


if __name__ == '__main__':
    irc_client = IRCClient()
    irc_client.run()
