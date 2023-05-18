from abc import ABC, abstractmethod


class UserInterface(ABC):
    def __init__(self, server_communicator):
        self.server_communicator = server_communicator

    @abstractmethod
    def display_output(self):
        pass

    @abstractmethod
    def display_input(self):
        pass
