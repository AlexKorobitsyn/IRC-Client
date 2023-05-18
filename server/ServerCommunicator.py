class ServerCommunicator:
    def __init__(self, serv_interact, user_interact):
        self.serv_interact = serv_interact
        self.user_interact = user_interact
        self.signal = True

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
            case "CHNGNICK":
                self.user_interact.change_nick()
                self.serv_interact.set_nickname(self.user_interact.nickname)
            case "CHNGCHANNEL":
                self.user_interact.change_channel()
                self.serv_interact.join_channel(self.user_interact.channel_name)
            case "HELP":
                print("THAT'S HELP, LOOK IN THE CODE")
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

    def output_from_server(self):
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