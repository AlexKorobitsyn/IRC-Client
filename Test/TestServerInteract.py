import socket
import unittest
from unittest.mock import patch, Mock

from server.ServerInteract import ServerInteract
from user.UserConfig import UserConfig


class ServerInteractTestCase(unittest.TestCase):

    def setUp(self):
        config = UserConfig()
        self.server_interact = ServerInteract(config)

    @patch('socket.socket')
    def test_connect(self, mock_socket):
        mock_sock = mock_socket.return_value
        self.server_interact.connect()
        mock_socket.assert_called_once_with(socket.AF_INET, socket.SOCK_STREAM)
        mock_sock.connect.assert_called_once_with((self.server_interact.config.ip, self.server_interact.config.port))
        mock_sock.settimeout.assert_called_once_with(0.2)

    @patch.object(ServerInteract, 'send_to_server')
    def test_take_names_in_channel(self, mock_send_to_server):
        channel = "test_channel"
        self.server_interact.take_names_in_channel(channel)
        mock_send_to_server.assert_called_once_with("NAMES", channel)

    @patch.object(ServerInteract, 'send_to_server')
    def test_write_private_msg(self, mock_send_to_server):
        address = "test_address"
        msg = "test_message"
        self.server_interact.write_private_msg(address, msg)
        mock_send_to_server.assert_called_once_with("PRIVMSG test_address :", msg)

    @patch.object(ServerInteract, 'send_to_server')
    def test_join_channel(self, mock_send_to_server):
        channel = "test_channel"
        self.server_interact.join_channel(channel)
        mock_send_to_server.assert_called_once_with("JOIN", channel)

    @patch.object(ServerInteract, 'send_to_server')
    def test_quit(self, mock_send_to_server):
        self.server_interact.quit()
        mock_send_to_server.assert_called_once_with("QUIT", "Good bye!")

    @patch.object(ServerInteract, 'send_to_server')
    def test_set_password(self, mock_send_to_server):
        self.server_interact.set_password()
        mock_send_to_server.assert_called_once_with("PASS", self.server_interact.config.password)

    @patch.object(ServerInteract, 'send_to_server')
    def test_set_nickname(self, mock_send_to_server):
        nickname = "test_nickname"
        self.server_interact.set_nickname(nickname)
        mock_send_to_server.assert_called_once_with("NICK", nickname)

    def test_get_response(self):
        expected_response = b"test_response"
        self.server_interact.sock = Mock()
        self.server_interact.sock.recv.return_value = expected_response
        response = self.server_interact.get_response()
        self.assertEqual(response, expected_response)
        self.server_interact.sock.recv.assert_called_once_with(1024)


if __name__ == '__main__':
    unittest.main()
