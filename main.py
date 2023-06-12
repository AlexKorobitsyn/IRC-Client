from IRCClient import IRCClient
import argparse


# irc.forestnet.org 7000 #elite-games

# TODO проблема с HISTORY в GUI
# TODO при закрытии стартового окна не по нажатию Connect че то делать
# TODO создавать кнопки в окне с помощью цикла: "for button : buttons..."
# TODO Сделать получение аргументов в WRITE не только после первого пробела
# TODO Сделать gui более читаемым
# TODO Реализовать добавление и создание каналов в channel_bar
# TODO мб сделать кнопки через self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
# TODO уйти от логики размещения виджетов через column's и row's
def main():
    irc_client = IRCClient()
    irc_client.run()


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='There is no need to pass arguments to this program.\n' +
                                                    'Available commands\n' +
                                                    '+ NAMES: Get a list of users in the current channel.\n' +
                                                    '+ LIST: Get a list of available channels on the server.\n' +
                                                    '+ JOIN: Join the specified channel.\n' +
                                                    '+ HISTORY: Download message history.\n' +
                                                    '+ CHNGNICK: Change nickname.\n' +
                                                    '+ CHNGCHANNEL: Change current channel.\n' +
                                                    '+ PRIVMSG: Send a private message to the user.\n' +
                                                    '+ QUIT: Quit the IRC client.\n')
    args = argparser.parse_args()
    main()
