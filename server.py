import socket
import threading
import pickle
from game import Game

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5555
DISCONNECT_MESSAGE = "!DISCONNECT"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind((SERVER, PORT))
except socket.error as e:
    print(str(e))

print("Server Started, Waiting for connections...")
server.listen()

games = {}
idCount = 0
player_id = 1

def take_action(user_data, game):
    """ Reads the data received from the client and do the action according to it """

    code = user_data.split(',')     # [action, player_ID, card_index]
    action = code[0]
    if len(code) > 1:
        p_id, card_index, p2_id, card2_index = int(code[1]), int(code[2]), int(code[3]), int(code[4])

    # deal 4 cards to each player
    if action == "deal":
        game.start_deal()

    # player finished turn
    if action == "Next_Turn":
        game.next_turn()
        print("Turn: ", game.get_turn())

    # player take card from dump and throw one from hand to dump
    if action == "dump_to_hand":
        game.dump_switch(p_id, card_index)

    # player take card from game deck and throw one from hand to dump
    if action == "deck_to_hand":
        game.deck_to_hand(p_id, 1, card_index)

    if action == "switch_cards":
        game.switch_cards(p_id, card_index, p2_id, card2_index)

    conn.sendall(pickle.dumps(game))

def handleClient(conn, p_id, gameId):
    global idCount
    conn.send(str.encode(str(p_id)))

    while True:
        try:
            data = conn.recv(2048).decode()
            if data != "None":
                print(f"User {p_id}: {data}")

            if gameId in games:
                game = games[gameId]

                if data == DISCONNECT_MESSAGE:
                    break

                conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        conn.send(str.encode(DISCONNECT_MESSAGE))
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()


while True:
    conn, addr = server.accept()
    print("Connected to:", addr)

    idCount += 1
    gameId = (idCount - 1) // 4

    if player_id > 4:
        player_id = 1

    # Already have 1 player and game settings exist but game has not started
    if idCount % 4 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game... waiting for players to join")

    # if we have 4 players in game
    elif idCount % 4 == 0:
        print("playing")
        games[gameId].start_deal()

    try:
        player_id = len(games[gameId].players)
        games[gameId].add_player(player_id)
    except Exception as e:
        print(e)

    thread = threading.Thread(target=handleClient, args=(conn, player_id, gameId))
    thread.start()

    """ arrange the idCount after client disconnect"""
    if len(games) > 0:
        key = (list(games.keys()))[-1]
        p_num = games[key].players_num()
        idCount = (key * 4) + p_num
