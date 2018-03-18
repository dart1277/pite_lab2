from unittest import TestCase

from game import models


class TestOXModel(TestCase):
    testModel = None

    def setUp(self):
        super().setUp()
        self.testModel = models.OXModel(0)

    def test_add_player(self):
        test_name = 'testName'
        test_id = 0

        self.testModel.add_player(test_name, test_id)

        self.assertEqual(test_name, self.testModel._OXModel__players[test_id])
        self.assertEqual('Player2', self.testModel._OXModel__players[1])

    def test_add_player_id_len_too_big(self):
        test_name = 'testName'
        test_id = 4

        self.testModel.add_player(test_name, test_id)

        self.assertEqual('Player 1', self.testModel._OXModel__players[0])
        self.assertEqual('Player2', self.testModel._OXModel__players[1])

    def test_add_player_id_negative(self):
        test_name = 'testName'
        test_id = -3

        self.testModel.add_player(test_name, test_id)

        self.assertEqual('Player 1', self.testModel._OXModel__players[0])
        self.assertEqual('Player2', self.testModel._OXModel__players[1])

    def test_get_players_count(self):
        self.fail()

    def test_get_current_player(self):
        self.fail()

    def test_get_board(self):
        self.fail()

    def test_make_move(self):
        self.fail()

    def test_check_game_result(self):
        self.fail()
