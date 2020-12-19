from network import *
import threading
import time


def connect():
    global CLIENT
    global ADDR
    try:
        CLIENT.connect(ADDR)
        return CLIENT.recv(2048).decode()
    except:
        print("Connection Failed")


def send(data):
    global CLIENT
    global game
    try:
        CLIENT.send(str.encode(data))
        game = pickle.loads(CLIENT.recv(2048))
    except socket.error as e:
        print(e)

def send_input():
    global CLIENT
    global game
    data = input(f"user {MY_ID}: ")
    try:
        CLIENT.send(str.encode(data))
        game = pickle.loads(CLIENT.recv(2048))
    except socket.error as e:
        print(e)

def is_runnig():
    global game_flag
    try:
        send("None")
    except:
        game_flag = False

def data_deck_to_hand(card_index):
    """ player_ID, action, card_index """
    global MY_ID
    code = "deck_to_hand" + ',' + str(MY_ID) + ',' + str(card_index) + ',' + '-1' + ',' + '-1'
    return code


def data_dump_to_hand(card_index):
    """ action, player_ID, card_index """
    global MY_ID
    code = "dump_to_hand" + ',' + str(MY_ID) + ',' + str(card_index) + ',' + '-1' + ',' + '-1'
    return code


def data_switch_cards(card1_index, hand2_id, card2_index):
    """ action, player_ID, card_index, player2_ID, card2_index """
    global MY_ID
    code = "switch_cards" + ',' + str(MY_ID) + ',' + str(card1_index) +',' + str(hand2_id) + ',' + str(card2_index)
    return code

def main():
    thread = threading.Thread(target=is_runnig)
    thread.start()

    print(MY_ID)

    if game == "dump":
        send(data_dump_to_hand(0))
    elif game == "deck":
        send(data_deck_to_hand(0))
    elif game == "S":
        send(data_switch_cards(0, 2, 0))


DISCONNECT_MESSAGE = "!DISCONNECT"
CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5555
ADDR = (SERVER, PORT)
MY_ID = connect()
game_flag = True    # If the game is going on or not
send("deal")


# while all 4 users in the game
while game_flag:
    main()
# when the game has ended or a player left the game
if not game_flag:
    print("End of game")
    time.sleep(5)