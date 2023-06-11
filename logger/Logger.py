import os
import datetime


class Logger:
    def __init__(self):
        self.path = os.path.join("logger", "log.txt")
        self.file = open(self.path, 'a+')

        self.buffer_size = 100000000
        self.data_from_history = ""

    def check_buffer_size(self):
        if os.stat(self.path).st_size > self.buffer_size:
            self.file.truncate()

    def save(self, data):
        self.check_buffer_size()
        date_now = datetime.datetime.now().__str__()
        if data != "":
            self.file.write("\n" + date_now + ":\n")
            self.file.write(data)

    def load(self):
        self.file.seek(0)
        self.data_from_history = self.file.read()
