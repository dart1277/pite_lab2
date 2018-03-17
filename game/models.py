import math


class OXModel:
    def __init__(self, game_id):
        self.__id = game_id
        self.__players = ['Player 1', 'Player2']
        self.__current_player = 0
        self.__board_len = 9
        self.__board = [-1 for i in range(0, self.__board_len)]

    def add_player(self, name, player_id):
        if len(self.__players) > player_id and type(player_id) == int and name:
            self.__players[player_id] = str(name)

    def get_current_player(self):
        return self.__players[self.__current_player]

    def get_board(self):
        return self.__board[:]

    def __is_move_valid(self, field):
        """validate field number and if the move is feasible"""
        if 0 <= field < len(self.__board) and self.__board[field] == -1:
            return True

    def __str_to_int(self, val):
        try:
            val = int(val)
            return val
        except ValueError:
            return

    def make_move(self, field):
        field = self.__str_to_int(field)
        if field is not None and self.__is_move_valid(field):
            self.__board[field] = self.__current_player
            self.__current_player = (self.__current_player + 1) % len(self.__players)
            return True

    def check_game_result(self):
        dim = int(math.sqrt(self.__board_len))
        result = None

        def board(i, j):
            return self.__board[i * dim + j]

        # mock answer
        if all(map(lambda x: x != -1, self.__board)):
            result = 'Done'
        return result
