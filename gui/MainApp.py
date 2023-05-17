import tkinter
import tkinter.messagebox
from user import UserInteract
import customtkinter

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class MainApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # configure window
        self.title("IRC клиент")
        self.geometry(f"{1000}x{600}+356+50")
        self.resizable(False, False)
        # configure col and row
        self.grid_columnconfigure((0, 1, 2, 3, 4), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        # create channel bar
        self.channel_bar_frame = customtkinter.CTkFrame(self, height=1000, width=150)
        self.channel_bar_frame.grid(row=0, column=0, rowspan=6)
        # create commands buttons
        self.user_button = customtkinter.CTkButton(self, text="USER")
        self.user_button.grid(row=4, column=1, padx=10)
        self.join_button = customtkinter.CTkButton(self, text="JOIN")
        self.join_button.grid(row=4, column=2, padx=10)
        self.help_button = customtkinter.CTkButton(self, text="HELP")
        self.help_button.grid(row=4, column=3, padx=10)
        self.quit_button = customtkinter.CTkButton(self, text="QUIT")
        self.quit_button.grid(row=4, column=4, padx=10)
        self.write_button = customtkinter.CTkButton(self, text="WRITE")
        self.write_button.grid(row=4, column=5, padx=10)
        self.privmsg_button = customtkinter.CTkButton(self, text="PRIVMSG")
        self.privmsg_button.grid(row=5, column=1, padx=10, pady=10)
        self.chngnick_button = customtkinter.CTkButton(self, text="CHNGNICK")
        self.chngnick_button.grid(row=5, column=2, padx=10, pady=10)
        self.chngchannel_button = customtkinter.CTkButton(self, text="CHNGCHANNEL")
        self.chngchannel_button.grid(row=5, column=3, padx=10, pady=10)
        self.ss_button = customtkinter.CTkButton(self, text="SS")
        self.ss_button.grid(row=5, column=4, padx=10, pady=10)
        self.names_button = customtkinter.CTkButton(self, text="NAMES")
        self.names_button.grid(row=5, column=5, padx=10, pady=10)
        # create output window
        #
        #
        # create sendall functional
        self.sendall_entry = customtkinter.CTkEntry(self, placeholder_text="Введите сообщение")
        self.sendall_entry.grid(row=3, column=1, padx=(20, 0), pady=(20, 20), columnspan=4, rowspan=1, sticky="nsew")
        self.sendall_button = customtkinter.CTkButton(self, text="sendall")
        self.sendall_button.grid(row=3, column=5, padx=10, pady=10)


if __name__ == '__main__':
    app = MainApp()
    app.mainloop()
