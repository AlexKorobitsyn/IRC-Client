import tkinter
import tkinter.messagebox
from User import UserInteract
import customtkinter

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class StartApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.ip = None
        self.port = None
        self.username = None
        self.password = None
        self.title("IRC клиент")
        self.geometry(f"{1000}x{600}+356+50")
        self.resizable(False, False)
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create welcome label
        self.hello_irc_frame = customtkinter.CTkFrame(self, width=1000, height=100, corner_radius=10)
        self.hello_irc_frame.grid(row=0, column=0, rowspan=1, columnspan=4, sticky="nsew")
        self.hello_irc_label = customtkinter.CTkLabel(self.hello_irc_frame, text="Welcome to IRC Client!",
                                                      font=customtkinter.CTkFont(size=28, weight="bold"),
                                                      text_color="#faaaaa", anchor="center")
        self.hello_irc_label.grid(padx=350, pady=(20, 10))
        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=300, height=400, corner_radius=10)
        self.sidebar_frame.grid(row=1, column=0, rowspan=3, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(0, weight=0)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Input parameters",
                                                 font=customtkinter.CTkFont(size=25, weight="bold"))
        self.logo_label.grid(padx=20, pady=(20, 10))
        self.ip_entry = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="IP")
        self.ip_entry.grid(padx=20, pady=20, sticky="nsew")
        self.port_entry = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Port")
        self.port_entry.grid(padx=20, pady=20, sticky="nsew")
        self.username_entry = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Username")
        self.username_entry.grid(padx=20, pady=20, sticky="nsew")
        self.password_entry = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Password")
        self.password_entry.grid(padx=20, pady=20, sticky="nsew")

        # create bar with well-known servers
        self.well_known_frame = customtkinter.CTkFrame(self, width=250, height=400, corner_radius=10)
        self.well_known_frame.grid(row=1, column=3, rowspan=3, sticky="nsew")
        self.well_known_label = customtkinter.CTkLabel(self.well_known_frame, text="Well known servers",
                                                       font=customtkinter.CTkFont(size=25, weight="bold"))
        self.well_known_label.grid(padx=20, pady=(20, 10))
        self.well_known_server1_button = customtkinter.CTkButton(self.well_known_frame, text="irc.forestnet.org 6667",
                                                                 command=self.well_known_server1_button_event,
                                                                 width=200, height=50)
        self.well_known_server1_button.grid(pady=10, padx=20)
        self.well_known_server2_button = customtkinter.CTkButton(self.well_known_frame, text="irc.forestnet.org 6667",
                                                                 command=self.well_known_server2_button_event,
                                                                 width=200, height=50)
        self.well_known_server2_button.grid(pady=10, padx=20)
        self.well_known_server3_button = customtkinter.CTkButton(self.well_known_frame, text="irc.forestnet.org 6667",
                                                                 command=self.well_known_server3_button_event,
                                                                 width=200, height=50)
        self.well_known_server3_button.grid(pady=10, padx=20)

        # create connect button
        self.connect_frame = customtkinter.CTkFrame(self, width=500, height=530, corner_radius=10)
        self.connect_frame.grid(row=1, column=1, rowspan=2, columnspan=2)
        self.connect_button = customtkinter.CTkButton(self.connect_frame, text="CONNECT",
                                                      command=self.connect_button_event, width=200, height=200)
        self.connect_button.grid(pady=170, padx=150)

    def well_known_server1_button_event(self):
        self.ip_entry.insert(0, "irc.forestnet.org")
        self.port_entry.insert(0, "6667")
        self.ip = "irc.forestnet.org"
        self.port = "6667"

    def well_known_server2_button_event(self):
        self.ip_entry.insert(0, "irc.forestnet.org")
        self.port_entry.insert(0, "6667")
        self.ip = "irc.forestnet.org"
        self.port = "6667"

    def well_known_server3_button_event(self):
        self.ip_entry.insert(0, "irc.forestnet.org")
        self.port_entry.insert(0, "6667")
        self.ip = "irc.forestnet.org"
        self.port = "6667"

    def connect_button_event(self):
        self.ip = self.ip_entry.get()
        self.port = self.port_entry.get()
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        self.destroy()


if __name__ == "__main__":
    app = StartApp()
    app.mainloop()
