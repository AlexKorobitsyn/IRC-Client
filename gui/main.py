import tkinter as tk


def handle_choice(choice):
    print("Выбран режим", choice)
    popup.destroy()


root = tk.Tk()

popup = tk.Toplevel(root)
popup.title("Выбор режима")

label = tk.Label(popup, text="Что вы хотите использовать?")
label.pack(padx=20, pady=10)

button_gui = tk.Button(popup, text="GUI", command=lambda: handle_choice("GUI"))
button_gui.pack(pady=5)

button_cui = tk.Button(popup, text="CUI", command=lambda: handle_choice("CUI"))
button_cui.pack(pady=5)

root.mainloop()
