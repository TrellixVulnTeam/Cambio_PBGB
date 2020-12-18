import socket
from _thread import *
import pickle
from game import *


def take_action(user_data, game):
    """ Reads the data received from the client and do the action according to it """

    print(user_data)
    code = user_data.split(',')     # [action, player_ID, card_index]
    action = code[0]
    if len(code) > 1:
        p_id, card_index = int(code[1]), int(code[2])

    # deal 4 cards to each player
    if action == "deal":
        game.start_deal()


    # player finished turn
    if action == "Next_Turn":
        game.next_turn()
        print("Turn: ", game.get_turn())

    # player take card from game deck and throw one from hand to dump
    if action == "deck_to_hand":
        game.deck_to_hand("gameDeck", player_id)
        game.hand_to_dump(p_id, int(code[2]))

    # player take card from dump and throw one from hand to dump
    if action == "dump_to_hand":
        game.dump_switch(int(p_id, card_index))

    if action == "deck_to_hand":
        game.deck_to_hand(p_id, 1, card_index)

    conn.sendall(pickle.dumps(game))


def threaded_client(conn, player_id, gameId):
    global idCount
    conn.send(str.encode(str(player_id)))

    while True:
        # print("key=",(list(games.keys())[-1]), " id=", idCount, " ,len: ", len(games))

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
    conn.close()
    if len(games) > 0:
        key = (list(games.keys()))[-1]
        pnum = len(games[key].players)
        idCount = ((list(games.keys()))[-1] * 4) + len(games[key].players)


def threaded_client2(conn, player_id, gameId):
    global idCount
    conn.send(str.encode(str(player_id)))

    while True:
        try:
            data = conn.recv(4096).decode()

            if gameId in games:
                game = games[gameId]

                if not data:
                    print("Not data")
                    break

                else:
                    take_action(data, game)

            else:
                break
        except:
            break

    print("Lost connection")
    try:
        # del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    print(idCount)
    conn.close()


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

# when we connect to a client
while True:
    conn, addr = socket1.accept()
    print("Connected to:", addr)

    idCount += 1
    gameId = (idCount - 1) // 4  # The 4 is the number of players in each game

    if player_id > 4:
        player_id = 1

    # number of players in a game
    if idCount % 4 == 1:  # The 4 is the number of players
        games[gameId] = Game(gameId)  # Creates a new Game settings and wait for another player
        # print("Creating a new game...")

    elif idCount % 4 == 0:  # Already have 1 player and game settings exist but game has not started
        games[gameId].ready = True
        print("playing")

    try:
        games[gameId].add_player()
        player_id = len(games[gameId].players)
    except:
        player_id = 0
        pass

    start_new_thread(threaded_client2, (conn, player_id, gameId))

    """ arrange the idCount after client disconnect """
    if len(games) > 0:
        key = (list(games.keys()))[-1]
        pnum = len(games[key].players)
        idCount = ((list(games.keys()))[-1] * 4) + len(games[key].players)
