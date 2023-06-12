from customtkinter import CTkToplevel
from tkinter import Tk, Text, Scrollbar


class HelpApp(CTkToplevel):
    def __init__(self, root, text):
        super().__init__(root)
        self.title("Help")
        self.geometry("400x300")

        self.text_box = Text(self, width=50, height=15)
        self.text_box.insert("end", text)
        self.text_box.configure(state="disabled")

        self.text_box.pack(expand=True, fill="both")
