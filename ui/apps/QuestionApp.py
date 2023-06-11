import tkinter as tk

from customtkinter import CTkToplevel


class QuestionApp(CTkToplevel):
    def __init__(self, root, question: str):
        super().__init__(root)

        self.title("Question")
        self.geometry("300x150")

        self.question_label = tk.Label(self, text=question)
        self.question_label.pack(pady=10)

        self.answer_entry = tk.Entry(self)
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_answer)
        self.submit_button.pack(pady=10)

        self.answer = None

    def submit_answer(self):
        self.answer = self.answer_entry.get()
        self.destroy()

    def get_answer(self):
        return self.answer
