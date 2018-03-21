from game.controller import Controller
import unittest
from unittest.mock import patch


class TestOxController(unittest.TestCase):

    @patch('game.controller.OXModel')
    @patch('game.controller.OXConsoleView')
    def test_controller_add_player(self, console_view_mock, model_mock):
        con = Controller()
        model_mock.return_value = model_mock
        model_mock.add_player.return_value = True  # Model's method must return sthg other than None, 0, False
        # unless we want the Controller to Call OXConsoleView.error
        console_view_mock.add_player.return_value = None
        g_id = con.get('get_new_game_instance', 0)
        out = con.get('add_player', g_id, 'name1', 0)
        self.assertEqual(out, None)  # console_view_mock.add_player.return_value == None
        model_mock.add_player.assert_called_with(model_mock, 'name1', 0)
        console_view_mock.add_player.assert_called_with(console_view_mock, model_mock, True)


if __name__ == '__main__':
    unittest.main()
