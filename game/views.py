class OXConsoleView:
    def error(self, model, result):
        return False

    def add_player(self, model, result):
        return result

    def get_current_player(self, model, result):
        return result

    def get_board(self, model, result):
        '''render a nice board here'''
        display_chars = ['O', 'X', ' ']
        board = list(map(lambda f: display_chars[f], result))
        for i in reversed(range(1, len(board))):
            ch = '|'
            if i % 3 == 0:
                ch = '\n-----\n'
            board.insert(i, ch)
        board.insert(0, '\n')
        board.append('\n')
        return ''.join(board)

    def make_move(self, model, result):
        return result

    def check_game_result(self, model, result):
        return result
