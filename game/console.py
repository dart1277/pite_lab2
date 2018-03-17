from game.controller import Controller


class OXGame:

    def __init__(self):
        self.controller = Controller()
        self.id = self._get_new_game_instance()

    def add_player(self, name, player_no):
        self.controller.get('add_player', self.id, name, player_no)

    def get_current_player(self):
        return self.controller.get('get_current_player', self.id)

    def get_board(self):
        return self.controller.get('get_board', self.id)

    def make_move(self, field):
        return self.controller.get('make_move', self.id, field)

    def _get_new_game_instance(self):
        return self.controller.get('get_new_game_instance', 0)

    def check_game_result(self):
        return self.controller.get('check_game_result', self.id)

    def end_game(self):
        self.controller.get('end_game', self.id)

    def play(self):
        player1 = input('Please enter yor name (Player 1)\n')
        player2 = input('Please enter yor name (Player 2)\n')
        self.add_player(player1, 0)
        self.add_player(player2, 1)
        result = None
        while not result:
            print(self.get_board())
            move_ok = False
            while not move_ok:
                move = input('Player ' + self.get_current_player() + ' enter next move\n')
                move_ok = self.make_move(move)
            result = self.check_game_result()
        print('Game Over!')
        print(self.get_board())
        print(result)
        self.end_game()
        print('Thank you.')


if __name__ == '__main__':
    game = OXGame()
    game.play()
