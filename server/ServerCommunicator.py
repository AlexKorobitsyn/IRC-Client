class ServerCommunicator:
    def __init__(self, serv_interact, user_interact):
        self.serv_interact = serv_interact
        self.user_interact = user_interact
        self.speaker = None
