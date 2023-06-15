import os
import unittest
import socket
from unittest.mock import patch, Mock

from server import AbstractSpeaker
from server.CommandSpeaker import CommandSpeaker
from server.ServerInteract import ServerInteract
from user.UserConfig import UserConfig
from user.UserInteract import UserInteract


class MyTestCase(unittest.TestCase):
    config = UserConfig()
    config.ip = 'example.com'
    config.port = 12345
    config.username = "test1"
    config.password = "12345"
    test_server_interact = ServerInteract(config)
    test_user_interact = UserInteract()
    test_user_interact.input_config(config)
    command_speaker = CommandSpeaker(test_server_interact, test_user_interact)

    def test_input_config_user_interact(self):
        self.assertEqual(self.config.ip, self.test_user_interact.config.ip)

    def test_input_config_server_interact(self):
        self.assertEqual(self.config.ip, self.test_server_interact.config.ip)


class CommandSpeakerTestCase(unittest.TestCase):

    def setUp(self):
        self.serv_interact_mock = Mock()
        self.user_interact_mock = Mock()
        self.speaker = CommandSpeaker(self.serv_interact_mock, self.user_interact_mock)

    @patch('builtins.input', side_effect=["test_channel"])
    def test_names_action(self, mock_input):
        self.speaker.names_action()
        self.serv_interact_mock.take_names_in_channel.assert_called_once_with("test_channel")

    @patch('builtins.input', side_effect=["test_address", "test_message"])
    def test_privmsg_action(self, mock_input):
        self.speaker.privmsg_action()
        self.serv_interact_mock.write_private_msg.assert_called_once_with("test_address", "test_message")

    @patch('builtins.input', return_value="test_nickname")
    def test_chngnick_action(self, mock_input):
        self.speaker.chngnick_action()
        self.user_interact_mock.change_nick.assert_called_once_with("test_nickname")
        self.serv_interact_mock.set_nickname.assert_called_once_with(self.user_interact_mock.nickname)

    @patch('builtins.input', return_value="test_channel")
    def test_chngchannel_action(self, mock_input):
        self.speaker.chngchannel_action()
        self.user_interact_mock.change_channel.assert_called_once_with("test_channel")
        self.serv_interact_mock.join_channel.assert_called_once_with(self.user_interact_mock.channel_name)

    @patch('builtins.input', side_effect=["test_command", "test_argument"])
    def test_write_action(self, mock_input):
        self.speaker.write_action()
        self.serv_interact_mock.send_to_server.assert_called_once_with("test_command", "test_argument")


if __name__ == '__main__':
    unittest.main()
