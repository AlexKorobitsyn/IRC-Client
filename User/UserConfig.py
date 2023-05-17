class UserConfig:
    def __init__(self):
        self._ip = None
        self._port = None
        self._username = None
        self._password = None

    @property
    def ip(self):
        return self._ip

    @property
    def port(self):
        return self._port

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @ip.setter
    def ip(self, value):
        self._ip = value

    @port.setter
    def port(self, value):
        self._port = int(value)

    @username.setter
    def username(self, value):
        self._username = value

    @password.setter
    def password(self, value):
        self._password = value
