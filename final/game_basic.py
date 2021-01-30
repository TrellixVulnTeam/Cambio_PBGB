class Game:
    def __init__(self, game_id, private=False):
        self.id = game_id  # The ID of the current game
        self.started = False  # If the game has started or still waiting for players
        self.players = {}  # The dict of the players in current game, key = client_data, value = hand
        self.names = {}    # The dict with the player's names
        self.private = private
        self.master = ()

    def get_id(self):
        return self.id

    def add_player(self, client, name):
        self.players[client.getpeername()] = "Yes"
        self.names[client.getpeername()] = name

        # If this client is the first
        if len(self.players) == 1:
            self.master = client.getpeername()

    def get_players(self):
        return self.players

    def remove_player(self, client):
        self.players.pop(client.getpeername())
        self.names.pop(client.getpeername())

        # If the master has disconnected put new master
        if self.master == client.getpeername():
            if len(self.players) > 0:
                keys = list(self.players.keys())
                self.master = keys[0]

    def get_players_num(self):
        return len(self.players)

    def is_private(self):
        return self.private

    def get_master(self):
        return self.master
