import os
from tkinter import Tk, Text, Entry, Button, messagebox, Scrollbar
from customtkinter import CTkToplevel
from server.AbstractSpeaker import AbstractSpeaker
from server.ServerCommunicator import ServerCommunicator
from playsound import playsound


class ChatApp(CTkToplevel):
    def __init__(self, root, speaker: AbstractSpeaker):
        super().__init__(root)
        self.speaker = speaker

        # configure window
        self.title("Chat App")
        self.geometry("800x600")

        # Создаем текстовое поле для отображения сообщений
        self.message_text = Text(self, width=100, height=30)
        self.message_text.pack()

        # Создаем поле для ввода текста
        self.input_entry = Entry(self, width=100)
        self.input_entry.pack(pady=10)

        # Создаем кнопку отправки сообщения
        self.send_button = Button(self, text="Send", command=self.send_command)
        self.send_button.pack()

        # Запускаем цикл получения сообщений с сервера
        self.after(1, self.get_server_response)

    def send_command(self):
        playsound(os.path.join('audio', 'click.mp3'), block=False)
        command = self.input_entry.get()
        self.input_entry.delete(0, 'end')
        self.speaker.commands_to_server(command)

    def get_server_response(self):
        if self.speaker.signal:
            try:
                if self.speaker.logger.data_from_history != "":
                    self.display_message(self.speaker.logger.data_from_history)
                    self.speaker.logger.data_from_history = ""
                    self.speaker.user_interact.had_history_to_load = False
                data = self.speaker.get_server_response()
                self.speaker.logger.save(data)
                self.display_message(data)
            except TimeoutError:
                pass
            self.after(100, self.get_server_response)
        else:
            self.destroy()

    def display_message(self, message):
        # Отображаем сообщение в текстовом поле
        playsound(os.path.join('audio', 'msg.wav'), block=False)
        self.message_text.configure(state="normal")
        self.message_text.insert("end", message + "\n")
        self.message_text.see("end")  # Прокручиваем текстовое поле до конца
        self.message_text.configure(state="disabled")
