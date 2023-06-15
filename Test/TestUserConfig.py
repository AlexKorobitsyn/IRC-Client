import unittest
from unittest.mock import patch, MagicMock

from user.UserConfig import UserConfig
from user.UserInteract import UserInteract


class UserInteractTestCase(unittest.TestCase):

    def setUp(self):
        self.user_interact = UserInteract()

    def test_change_nick(self):
        self.user_interact.change_nick('test_nickname')
        self.assertEqual(self.user_interact.nickname, 'test_nickname')

    def test_change_channel(self):
        self.user_interact.change_channel('test_channel')
        self.assertEqual(self.user_interact.channel_name, 'test_channel')

    def test_input_config(self):
        config = UserConfig()
        config.ip = '127.0.0.1'
        config.port = 8080
        config.username = 'test_user'
        config.password = 'test_password'
        self.user_interact.input_config(config)
        self.assertEqual(self.user_interact.config, config)


if __name__ == '__main__':
    unittest.main()