from tkinter import Tk, Text, Entry, Button, messagebox, Scrollbar
from customtkinter import CTkToplevel

from server.ServerCommunicator import ServerCommunicator


class OutputApp(CTkToplevel):
    def __init__(self, root, speaker):
        super().__init__(root)
        self.speaker = speaker
        self.title("OutputApp")
        self.geometry("800x600")

        # Создаем текстовое поле для отображения сообщений
        self.message_text = Text(self, width=100, height=100)
        self.message_text.pack()

        # Запускаем цикл получения сообщений с сервера
        self.after(1, self.get_server_response)

    def get_server_response(self):
        try:
            data = self.speaker.get_server_response()
            self.display_message(data)
        except TimeoutError:
            pass
        self.after(100, self.get_server_response)

    def display_message(self, message):
        # Отображаем сообщение в текстовом поле
        self.message_text.insert("end", message + "\n")
        self.message_text.see("end")  # Прокручиваем текстовое поле до конца
