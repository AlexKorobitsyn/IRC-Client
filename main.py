from IRCClient import IRCClient


# irc.forestnet.org 7000 #elite-games

# TODO сделать репозиторий приватным
# TODO Реализовать GUI
# TODO создавать кнопки в окне с помощью цикла: "for button : buttons..."
# TODO Сделать в output_from_server выбор print или вывод на GUI
# TODO Сделать README, изменить HELP
# TODO Сделать получение аргументов в WRITE не только после первого пробела
# TODO Сделать gui более читаемым
# TODO Сделать порядок кнопок команд, в MainApp, более логичный
# TODO Реализовать добавление и создание каналов в channel_bar
# TODO мб сделать кнопки через self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
# TODO дизайн gui
# TODO место вывода
# TODO уйти от логики размещения виджетов через column's и row's
def main():
    irc_client = IRCClient()
    irc_client.run()


if __name__ == '__main__':
    main()
