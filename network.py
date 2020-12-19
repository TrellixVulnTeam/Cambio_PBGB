import socket
import pickle
from game import Game


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.gethostbyname(socket.gethostname())
        self.port = 5555
        self.addr = (self.server, self.port)
        self.player = self.connect()

    def get_player(self):

        return self.player

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)

    def send_game(self, game):
        try:
            data = pickle.dumps(game)
            self.client.send(data)
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)
