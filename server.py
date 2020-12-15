import socket
from _thread import *
import pickle
from game import Game

# Need to change number of players allowed in a game to the number when they press start


server = "192.168.239.2"
port = 5555

socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket1.bind((server, port))
except socket.error as e:
    str(e)

socket1.listen(4)  # unable 4 players in each socket
print("Server Started, Waiting for connections...")

connected = set()
games = {}
idCount = 0
player_id = 0


def threaded_client(conn, player_id, gameId):
    global idCount
    conn.send(str.encode(str(player_id)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

            if gameId in games:
                game = games[gameId]

                if not data:
                    print("Not data")
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(player_id, data)

                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    idCount -= 1
    conn.close()


# when we connect to a client
while True:
    conn, addr = socket1.accept()
    print("Connected to:", addr)

    idCount += 1
    player_id += 10
    gameId = (idCount - 1) // 4  # The 4 is the number of players in each game
    # gameId = (idCount - 1) // num_of_current_game_players

    # number of players in a game
    if idCount % 4 == 1:  # The 4 is the number of players
        games[gameId] = Game(gameId)  # Creates a new Game settings and wait for another player
        games[gameId].add_player()
        print("Creating a new game...")

    elif idCount % 4 == 0:  # Already have 1 player and game settings exist but game has not started
        games[gameId].ready = True
        games[gameId].add_player()
        print("playing")
        player_id = 0
    else:
        games[gameId].add_player()

    start_new_thread(threaded_client, (conn, player_id, gameId))
    print("Hands num: ", len(games[gameId].players))
