import tkinter
from tkinter import Tk, Label, Entry, Button, messagebox

from server.ServerCommunicator import ServerCommunicator


class ChannelInfoApp(Tk):
    def __init__(self, server_communicator: ServerCommunicator):
        super().__init__()
        self.server_communicator = server_communicator

        # window configure
        self.title("Channel Information")
        self.geometry("400x300")  # Установите желаемый размер окна

        # Метка и поле ввода для канала
        channel_label = Label(self, text="Channel Name:")
        channel_label.pack()
        self.channel_entry = Entry(self)
        self.channel_entry.pack()

        # Метка и поле ввода для никнейма
        nickname_label = Label(self, text="Nickname:")
        nickname_label.pack()
        self.nickname_entry = Entry(self)
        self.nickname_entry.pack()

        # Кнопка JOIN
        join_button = Button(self, text="JOIN", command=self.join_channel)
        join_button.pack(side=tkinter.TOP, pady=10)

        # Список популярных каналов
        popular_channels_label = Label(self, text="Popular Channels:")
        popular_channels_label.pack()

        popular_channels = ["#elite-games", "#prog-rock", "#rus_news"]

        for channel in popular_channels:
            button = Button(self, text=channel, command=lambda ch=channel: self.fill_channel_entry(ch))
            button.pack()

    def fill_channel_entry(self, channel):
        self.channel_entry.delete(0, "end")
        self.channel_entry.insert(0, channel)

    def join_channel(self):
        channel_name = self.channel_entry.get()
        nickname = self.nickname_entry.get()
        if channel_name and nickname:
            self.server_communicator.user_interact.channel_name = channel_name
            self.server_communicator.user_interact.nickname = nickname
            self.destroy()
        else:
            messagebox.showerror("Error", "Please enter channel name and nickname.")
