import socket
import select
from game_basic import *
import pickle
import threading
import random


def create_room(client_conn, private=False):
    """ Called when the client asks to open a private room"""
    global games
    remove_double_games(client_conn)

    game_id = str(random.randint(100, 999))

    # If game room is available
    if game_id not in games.keys():
        games[game_id] = Game(game_id, private)
        games[game_id].add_player(client_conn)
        print(client_conn.getpeername(), "- Created room", game_id)
        client_conn.send(f"You created a new room|{game_id}".encode())
    # If room is not available try again
    else:
        create_room(client_conn, private)


def join_private_room(client_conn, game_id='0'):
    """ Called when the client asks to connect to a private room"""
    global games
    remove_double_games(client_conn)

    if game_id in games.keys() and games[game_id].get_players_num() < 4:
        games[game_id].add_player(client_conn)
        print(client_conn.getpeername(), f"- Joined room", game_id)
        client_conn.send(f"You joined room|{game_id}".encode())
        return
    # If game id is wrong
    else:
        client_conn.send("No such room available|Error".encode())
        return

    client_conn.send("No rooms available|Error".encode())


def join_random_room(client_conn):
    """ Called when the client asks to connect to any room available"""
    remove_double_games(client_conn)

    # Goes through all the rooms
    for temp_id in games.keys():
        # If room is available
        if not games[temp_id].is_private() and games[temp_id].get_players_num() < 4:
            games[temp_id].add_player(client_conn)
            print(client_conn.getpeername(), "- Joined room", temp_id)
            client_conn.send(f"You joined room|{temp_id}".encode())
            return
    client_conn.send("No rooms available - creating new room|Error".encode())


def player_in_room(client_conn):
    """
    gets a client and returns the game_id that the client is connected to
    returns "None" if client is not connected
    """
    # Going through all the games
    for game_id in games.keys():
        # if player is part of this game
        if client_conn.getpeername() in games[game_id].get_players().keys():
            return game_id
    return False


# Checks if player is connected to a game and disconnects him
def remove_double_games(client_conn):
    game_num = player_in_room(client_conn)

    if game_num:
        games[game_num].remove_player(client_conn)

        # If the room is empty
        if games[game_num].get_players_num() == 0:
            games.pop(game_num)
            print("Closed room:", game_num)


def handle_logout(current_socket, game_num):
    """ handles the logout of a client """
    # If player is connected to a game
    if game_num:
        games[game_num].remove_player(current_socket)

        # If the room is empty
        if games[game_num].get_players_num() == 0:
            games.pop(game_num)
            print("Closed room:", game_num)

    print("Disconnect client -", current_socket.getpeername())
    client_sockets.remove(current_socket)
    current_socket.close()


# Creates the server
def create_server():
    """ Sets the stats of the server and handles all connection with the clients """

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    print("Server is running!")
    server_socket.listen()
    print("Waiting for clients...")
    return server_socket


def handle_connections_msg(current_socket, data, game_num):
    """ handles all the data that is received from the player when he isn't connected to a room """

    # If client want to disconnect
    if data[0] == "Quit":
        handle_logout(current_socket, game_num)
        return

    if data[0] == "new":
        create_room(current_socket, private=False)
        return

    elif data[0] == "join":
        join_private_room(current_socket, game_id=data[1])
        return

    elif data[0] == "random":
        join_random_room(current_socket)
        return


def handle_client_game_msgs(current_socket, data, game_num):
    """ handles all the player actions in the game """
    if data[0] == "get_players_num" and game_num:
        snd_message = "Num of players|" + str(games[game_num].get_players_num())
        current_socket.send(snd_message.encode())
        return

    if data[0] == "get_game":
        current_socket.sendall(pickle.dumps(games[game_num]))
    pass


def connected_client_server_handle(current_socket):
    try:  # If the client has been disconnected an error will pop
        data = (current_socket.recv(MAX_MSG_LENGTH).decode()).split('|')
        game_num = player_in_room(current_socket)  # game_id the player is connected to (False if none)

        # If the player is already in a room
        if game_num:
            handle_client_game_msgs(current_socket, data, game_num)

        else:
            handle_connections_msg(current_socket, data, game_num)


    # Client has probably suddenly disconnected
    except Exception as e:
        print(e)
        game_num = player_in_room(
            current_socket)  # The game_id which the player is connected to (False if none)
        handle_logout(current_socket, game_num)


def main(server_socket):
    # Checking if sockets are changed status
    while True:
        ready_to_read, ready_to_write, in_error = select.select([server_socket] + client_sockets, [], [])

        # Going through all the clients that want to connect or already connected the server
        for current_socket in ready_to_read:
            # If its a client that asking to connect to the server
            if current_socket is server_socket:
                (client_conn, client_address) = server_socket.accept()
                print("New connection from: ", client_address)
                client_sockets.append(client_conn)

            # So it is an already connected client that has sent a massage
            else:
                #thread = threading.Thread(target=connected_client_server_handle, args=(current_socket,))
                #thread.start()
                connected_client_server_handle(current_socket)


# Server variables
SERVER_IP = "0.0.0.0"
SERVER_PORT = 4457
MAX_MSG_LENGTH = 1024

# Variables
send_message = ""  # The massage we want to send to the client
rec_data = ""  # The massage we receive from the client
client_sockets = []  # List of all the clients that are connected to our server
waiting_list = []  # List of players
games = {}


socket = create_server()
main(socket)
