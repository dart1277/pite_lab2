from game.models import OXModel
from game.views import OXConsoleView


class Controller:
    def __init__(self):
        self.__default_view = OXConsoleView
        self.__actions = {'add_player': {'model': OXModel.add_player,
                                         'view': self.__default_view.add_player,
                                         'error_view': self.__default_view.error
                                         },
                          'get_current_player': {'model': OXModel.get_current_player,
                                                 'view': self.__default_view.get_current_player,
                                                 'error_view': self.__default_view.error
                                                 },
                          'get_board': {'model': OXModel.get_board,
                                        'view': self.__default_view.get_board,
                                        'error_view': self.__default_view.error
                                        },
                          'make_move': {'model': OXModel.make_move,
                                        'view': self.__default_view.make_move,
                                        'error_view': self.__default_view.error
                                        },
                          'get_new_game_instance': {'model': OXModel,
                                                    'view': None,
                                                    'error_view': None
                                                    },
                          'check_game_result': {'model': OXModel.check_game_result,
                                                'view': self.__default_view.check_game_result,
                                                'error_view': self.__default_view.error
                                                },
                          'end_game': {'model': None,
                                       'view': None,
                                       'error_view': None
                                       }
                          }
        self.__games = {}
        self.__game_guid = 0

    def get(self, action, game_id, *params):
        if action in self.__actions and game_id in self.__games:
            if action == 'end_game':
                del self.__games[game_id]
                return
            result = self.__actions[action]['model'](self.__games[game_id], *params)
            if result and self.__actions[action]['view']:
                return self.__actions[action]['view'](self.__default_view, self.__games[game_id], result)
            elif not result and self.__actions[action]['error_view']:
                return self.__actions[action]['error_view'](self.__default_view, self.__games[game_id], result)
        elif action == 'get_new_game_instance':
            self.__game_guid = self.__game_guid + 1
            if self.__game_guid in self.__games:
                raise OverflowError('Too many games')
            self.__games[self.__game_guid] = self.__actions[action]['model'](game_id)
            return self.__game_guid
        else:
            pass  # Display action Error
