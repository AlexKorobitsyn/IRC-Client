import os

from playsound import playsound

from server.AbstractSpeaker import AbstractSpeaker


class CommandSpeaker(AbstractSpeaker):

    def __init__(self, serv_interact, user_interact):
        super().__init__(serv_interact, user_interact)

    def help_action(self, text):
        print(text)

    def names_action(self):
        channel = input("input channel name:\n")
        self.serv_interact.take_names_in_channel(channel)

    def privmsg_action(self):
        address = input("Message for Who?:")
        msg = input("Write your message:")
        self.serv_interact.write_private_msg(address, msg)

    def quit_action(self):
        playsound(os.path.join('audio', 'end.wav'), block=False)
        self.serv_interact.quit()
        self.serv_interact.sock.close()
        self.signal = False
        print("Quitting ...")
        exit(0)

    def chngnick_action(self):
        nickname = input("Input new Nickname:\n")
        self.user_interact.change_nick(nickname)
        self.serv_interact.set_nickname(self.user_interact.nickname)

    def chngchannel_action(self):
        channel = input("Input new Channel name:\n")
        self.user_interact.change_channel(channel)
        self.serv_interact.join_channel(self.user_interact.channel_name)

    def write_action(self):
        command = input("Write command:")
        arg = input("Write argument:")
        self.serv_interact.send_to_server(command, arg)
