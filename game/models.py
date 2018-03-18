import math


class OXModel:
    def __init__(self, game_id):
        self.__id = game_id
        self.__players = ['Player 1', 'Player2']
        self.__current_player = 0
        self.__board_len = 9
        self.__board = [-1 for it in range(0, self.__board_len)]

    def add_player(self, name, player_id):
        if len(self.__players) > player_id and type(player_id) == int and name:
            self.__players[player_id] = str(name)

    def get_players_count(self):
        return len(self.__players)

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

        class FoundException(Exception):
            pass

        def board(i, j):
            return self.__board[i * dim + j]

        def row(i):
            return self.__board[i * dim: i * dim + dim]

        def col(i):
            return [self.__board[j * dim + i] for j in range(0, dim)]

        def diag():
            return [self.__board[j * dim + j] for j in range(0, dim)]

        def diag2():
            return [self.__board[j * dim + dim - j - 1] for j in range(0, dim)]

        def check_slice(sli):  # validation: min == max != -1 (for row,column,diagonal), then winner == min
            if max(sli) == min(sli) != -1:
                raise FoundException(self.__players[min(sli)])

        try:
            for i in range(0, dim):
                check_slice(row(i))
                check_slice(col(i))
            check_slice(diag())
            check_slice(diag2())
            if all(map(lambda x: x != -1, self.__board)):
                result = 'A draw'
        except FoundException as e:
            result = str(e) + ' won the game!'
        return result
