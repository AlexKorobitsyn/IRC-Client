from abc import ABC, abstractmethod


class UserInterface(ABC):
    def __init__(self, speaker):
        self.speaker = speaker

    @abstractmethod
    def display_output(self):
        pass

    @abstractmethod
    def display_input(self):
        pass

    @abstractmethod
    def input_channel_info(self):
        pass
