from customtkinter import *
import asyncio
from playsound import playsound
from ui.apps.PopupMsgCreator import PopupMsgCreator
from user.UserConfig import UserConfig

set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class StartApp(CTkToplevel):
    def __init__(self, root):
        super().__init__(root)
        # configure window
        self.user_config = UserConfig()

        self.title("IRC клиент")
        self.geometry(f"{1000}x{600}+356+50")
        self.resizable(False, False)
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        # create welcome label
        self.hello_irc_frame = CTkFrame(self, width=1000, height=100, corner_radius=10)
        self.hello_irc_label = CTkLabel(self.hello_irc_frame, text="Welcome to IRC Client!",
                                        font=CTkFont(size=28, weight="bold"),
                                        text_color="#faaaaa", anchor="center")
        self.fill_welcome_label()
        # create sidebar frame with widgets
        self.sidebar_frame = CTkFrame(self, width=300, height=400, corner_radius=10)
        self.logo_label = CTkLabel(self.sidebar_frame, text="Input parameters",
                                   font=CTkFont(size=25, weight="bold"))
        self.ip_entry = CTkEntry(self.sidebar_frame, placeholder_text="IP")
        self.port_entry = CTkEntry(self.sidebar_frame, placeholder_text="Port")
        self.username_entry = CTkEntry(self.sidebar_frame, placeholder_text="Username")
        self.password_entry = CTkEntry(self.sidebar_frame, placeholder_text="Password")
        self.fill_sidebar_frame()
        # create bar with well-known servers
        self.well_known_frame = CTkFrame(self, width=250, height=400, corner_radius=10)
        self.well_known_label = CTkLabel(self.well_known_frame, text="Well known servers",
                                         font=CTkFont(size=25, weight="bold"))
        self.well_known_server1_button = CTkButton(self.well_known_frame, text="irc.forestnet.org 7000",
                                                   command=self.well_known_server1_button_event,
                                                   width=200, height=50)
        self.well_known_server2_button = CTkButton(self.well_known_frame, text="irc.forestnet.org 7000",
                                                   command=self.well_known_server2_button_event,
                                                   width=200, height=50)
        self.well_known_server3_button = CTkButton(self.well_known_frame, text="irc.forestnet.org 6667",
                                                   command=self.well_known_server3_button_event,
                                                   width=200, height=50)
        self.fill_well_known_servers_frame()
        # create connect button
        self.connect_frame = CTkFrame(self, width=500, height=530, corner_radius=10)
        self.connect_button = CTkButton(self.connect_frame, text="CONNECT",
                                        command=self.connect_button_event, width=200, height=200)
        self.fill_connect_button()

    def fill_welcome_label(self):
        self.hello_irc_frame.grid(row=0, column=0, rowspan=1, columnspan=4, sticky="nsew")
        self.hello_irc_label.grid(padx=350, pady=(20, 10))

    def fill_sidebar_frame(self):
        self.sidebar_frame.grid(row=1, column=0, rowspan=3, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(0, weight=0)

        self.logo_label.grid(padx=20, pady=(20, 10))

        self.ip_entry.grid(padx=20, pady=20, sticky="nsew")
        self.port_entry.grid(padx=20, pady=20, sticky="nsew")
        self.username_entry.grid(padx=20, pady=20, sticky="nsew")
        self.password_entry.grid(padx=20, pady=20, sticky="nsew")

    def fill_well_known_servers_frame(self):
        self.well_known_frame.grid(row=1, column=3, rowspan=3, sticky="nsew")

        self.well_known_label.grid(padx=20, pady=(20, 10))

        self.well_known_server1_button.grid(pady=10, padx=20)

        self.well_known_server2_button.grid(pady=10, padx=20)

        self.well_known_server3_button.grid(pady=10, padx=20)

    def fill_connect_button(self):
        self.connect_frame.grid(row=1, column=1, rowspan=2, columnspan=2)

        self.connect_button.grid(pady=170, padx=150)

    def well_known_server1_button_event(self):
        playsound(os.path.join('audio', 'click.mp3'), block=False)
        self.ip_entry.delete(0, len(self.ip_entry.get()))  # Удаляем существующий текст
        self.ip_entry.insert(0, "irc.forestnet.org")  # Вставляем новый текст
        self.port_entry.delete(0, len(self.ip_entry.get()))  # Удаляем существующий текст
        self.port_entry.insert(0, "7000")  # Вставляем новый текст
        self.user_config.ip = "irc.forestnet.org"
        self.user_config.port = "7000"

    def well_known_server2_button_event(self):
        playsound(os.path.join('audio', 'click.mp3'), block=False)
        self.ip_entry.delete(0, len(self.ip_entry.get()))  # Удаляем существующий текст
        self.ip_entry.insert(0, "irc.forestnet.org")  # Вставляем новый текст
        self.port_entry.delete(0, len(self.ip_entry.get()))  # Удаляем существующий текст
        self.port_entry.insert(0, "7000")  # Вставляем новый текст
        self.user_config.ip = "irc.forestnet.org"
        self.user_config.port = "7000"

    def well_known_server3_button_event(self):
        playsound(os.path.join('audio', 'click.mp3'), block=False)
        self.ip_entry.delete(0, len(self.ip_entry.get()))  # Удаляем существующий текст
        self.ip_entry.insert(0, "irc.forestnet.org")
        self.port_entry.delete(0, len(self.ip_entry.get()))  # Удаляем существующий текст
        self.port_entry.insert(0, "6667")
        self.user_config.ip = "irc.forestnet.org"
        self.user_config.port = "6667"

    def connect_button_event(self):
        playsound(os.path.join('audio', 'click.mp3'), block=False)
        self.user_config.ip = self.ip_entry.get()
        self.user_config.port = self.port_entry.get()
        self.user_config.username = self.username_entry.get()
        self.user_config.password = self.password_entry.get()
        self.destroy()


if __name__ == "__main__":
    root_window = CTk()
    app = StartApp(root_window)
    app.mainloop()
