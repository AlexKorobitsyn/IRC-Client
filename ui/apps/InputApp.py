from tkinter import Tk, Text, Entry, Button, messagebox
from customtkinter import CTkToplevel

from server.AbstractSpeaker import AbstractSpeaker
from server.ServerCommunicator import ServerCommunicator



class InputApp(CTkToplevel):
    def __init__(self, root, speaker: AbstractSpeaker):
        super().__init__(root)
        self.speaker = speaker



        # configure window
        self.title("Input App")
        self.geometry("400x200")
        self.resizable(False, False)

        # create input widgets
        self.input_entry = Entry(self)
        self.input_entry.pack(pady=10)

        self.send_button = Button(self, text="Send", command=self.send_command)
        self.send_button.pack()

    def send_command(self):
        command = self.input_entry.get()
        self.input_entry.delete(0, 'end')
        self.speaker.commands_to_server(command)
