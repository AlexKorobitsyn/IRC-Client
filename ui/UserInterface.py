from abc import ABC, abstractmethod


class UserInterface(ABC):
    def __init__(self, speaker):
        self.speaker = speaker

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def input_channel_info(self):
        pass
