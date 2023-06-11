import os

from playsound import playsound

from logger.Logger import Logger




class ServerCommunicator:
    def __init__(self, serv_interact, user_interact):
        self.serv_interact = serv_interact
        self.user_interact = user_interact
        self.signal = True
        self.logger = Logger()


    def commands_to_server(self, cmd):
        match cmd:
            case "NAMES":
                self.serv_interact.take_names_in_channel()
            case "LIST":
                self.serv_interact.take_channel_list()
            case "JOIN":
                self.serv_interact.join_channel(self.user_interact.channel_name)
            case "HISTORY":
                self.logger.load()
                self.user_interact.have_history_to_load = True
            case "CHNGNICK":
                self.user_interact.change_nick()
                self.serv_interact.set_nickname(self.user_interact.nickname)
            case "CHNGCHANNEL":
                self.user_interact.change_channel()
                self.serv_interact.join_channel(self.user_interact.channel_name)
            case "PRIVMSG":
                self.serv_interact.write_private_msg()
            case "QUIT":
                playsound(os.path.join('audio', 'end.wav'), block=False)
                self.serv_interact.quit()
                self.serv_interact.sock.close()
                self.signal = False
                exit(0)
            case "WRITE":
                command = input("Write command:")
                arg = input("Write argument:")
                self.serv_interact.send_to_server(command, arg)

    def get_server_response(self):
        data = self.serv_interact.get_response().decode('cp1251')
        if "PING" in data:
            self.serv_interact.send_to_server("PONG", ":" + data.split(":")[1])
        return data
