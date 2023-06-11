import os
from playsound import playsound
from logger.Logger import Logger
from abc import ABC, abstractmethod
from server.ServerInteract import ServerInteract
from user.UserInteract import UserInteract


class AbstractSpeaker(ABC):
    def __init__(self, serv_interact: ServerInteract, user_interact: UserInteract):
        self.signal = True
        self.logger = Logger()
        self.serv_interact = serv_interact
        self.user_interact = user_interact

    def commands_to_server(self, cmd):
        match cmd:
            case "NAMES":
                self.names_action()
            case "LIST":
                self.list_action()
            case "JOIN":
                self.join_action()
            case "HISTORY":
                self.history_action()
            case "CHNGNICK":
                self.chngnick_action()
            case "CHNGCHANNEL":
                self.chngchannel_action()
            case "PRIVMSG":
                self.privmsg_action()
            case "QUIT":
                self.quit_action()
            case "WRITE":
                self.write_action()

    @abstractmethod
    def names_action(self):
        pass

    def list_action(self):
        self.serv_interact.take_channel_list()

    def join_action(self):
        self.serv_interact.join_channel(self.user_interact.channel_name)

    def history_action(self):
        self.logger.load()
        self.user_interact.have_history_to_load = True

    @abstractmethod
    def chngnick_action(self):
        pass

    @abstractmethod
    def chngchannel_action(self):
        pass

    @abstractmethod
    def privmsg_action(self):
        pass

    @abstractmethod
    def quit_action(self):
        pass

    @abstractmethod
    def write_action(self):
        pass

    def get_server_response(self):
        data = self.serv_interact.get_response().decode('cp1251')
        if "PING" in data:
            self.serv_interact.send_to_server("PONG", ":" + data.split(":")[1])
        return data
