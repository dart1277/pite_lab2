import socket
from urllib import parse
from game.OXServer import OXServer


class OXControllerNetworkClient:
    TCP_IP = '127.0.0.1'
    TCP_PORT = OXServer.TCP_PORT
    BUFFER_SIZE = OXServer.BUFFER_SIZE

    def get(self, **params):
        query_str = parse.urlencode(params)
        data = s = None
        request_not_completed = True
        while request_not_completed:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((self.TCP_IP, self.TCP_PORT))
                s.send(query_str.encode())
                data = s.recv(self.BUFFER_SIZE)
                if len(data) == 0:
                    data = None
                else:
                    data = data.decode(encoding='UTF-8')
                request_not_completed = False
            except:
                print('Error: Cannot connect to the server!')
                try_again = input('Do you want to try again? Please press enter to confirm or type N to exit.\n')
                if len(try_again) > 0:
                    exit(1)
                print('Please wait...')
            finally:
                s.close()
        return data
