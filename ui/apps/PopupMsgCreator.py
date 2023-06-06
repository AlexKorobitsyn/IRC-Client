import os

import customtkinter as ctk
from playsound import playsound


class PopupMsgCreator:
    def __init__(self):
        pass

    @staticmethod
    def create_choice_of_two_options(question: str, option1: str, option2: str):
        PopupMsgCreator.choice = None

        def handle_choice(option):
            playsound(os.path.join('audio', 'click.mp3'), block=False)
            popup.destroy()
            PopupMsgCreator.choice = option

        popup = ctk.CTkToplevel()

        popup.title("Выбор")

        label = ctk.CTkLabel(popup, text=question)
        label.pack(padx=20, pady=10)

        button_gui = ctk.CTkButton(popup, text=option1, command=lambda: handle_choice(option1))
        button_gui.pack(pady=5)

        button_cui = ctk.CTkButton(popup, text=option2, command=lambda: handle_choice(option2))
        button_cui.pack(pady=5)

        PopupMsgCreator.set_in_center(popup)
        popup.wait_window()
        return PopupMsgCreator.choice

    @staticmethod
    def set_in_center(window):
        # Получение размеров экрана
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        # Расчет центральных координат окна
        window_width = window.winfo_width()
        window_height = window.winfo_height()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Установка положения окна по центру экрана
        window.geometry(f"+{x}+{y}")


if __name__ == '__main__':
    p = PopupMsgCreator()
    p.create_choice_of_two_options("34", "23523", "235")
