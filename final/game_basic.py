class Game:
    def __init__(self, game_id, private=False):
        self.id = game_id  # The ID of the current game
        self.started = False  # If the game has started or still waiting for players
        self.players = {}  # The dict of the players in current game, key = client_data, value = hand
        self.private = private
        self.master = ()

    def add_player(self, client, master="no"):
        self.players[client.getpeername()] = "Yes"

        if master == "master":
            self.master = client.getpeername()

    def get_players(self):
        return self.players

    def remove_player(self, client):
        self.players.pop(client.getpeername())

    def get_players_num(self):
        return len(self.players)

    def is_private(self):
        return self. private

