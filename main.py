from IRCClient import IRCClient
from gui import StartApp
from user import UserInteract
from server import ServerInteract
import threading


# irc.forestnet.org 7000 #elite-games

# TODO сделать репозиторий приватным
# TODO Сделать README, изменить HELP
# TODO обновление а не дописывание текста в gui
# TODO Сделать получение аргументов в WRITE не только после первого пробела
# TODO Сделать выбор режима gui или CUI?
# TODO Сделать gui более читаемым
# TODO Сделать порядок кнопок команд, в MainApp, более логичный
# TODO Реализовать добавление и создание каналов в channel_bar
# TODO мб сделать кнопки через self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
# TODO дизайн gui
# TODO вынести работу с MainApp на отдельный поток
# TODO место вывода
# TODO разбить работу gui на более читаемые методы
# TODO уйти от логики размещения виджетов через column's и row's
def main():
    irc_client = IRCClient()
    irc_client.run()


if __name__ == '__main__':
    main()
