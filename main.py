from IRCClient import IRCClient
import argparse


# irc.forestnet.org 7000 #elite-games

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
