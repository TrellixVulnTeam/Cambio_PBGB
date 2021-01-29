import socket
from tkinter import *
import pickle
from tkinter import messagebox

def msg_code(type, action, rival_id=" ", card1_id=" ", card2_id=" "):
    """
    return STR code for server that represents what you want to do in the game
    :type - connect (before game connection actions) / action (In game actions) / Quit
    :action - new / join / random / switch / dump_to_hand / deck_to_hand / switch_cards / deal / next_Turn
    :return - type|action|rival_id|card1_id|card2_id
    """
    return type + '|' + action + '|' + str(rival_id) + '|' + str(card1_id) + '|' + str(card2_id)


def start_game():
    pass


def get_game():
    #msg = msg_code("action", "get_game")
    msg = "get_game"
    my_socket.send(msg.encode())
    my_game = pickle.loads(my_socket.recv(2048))
    return my_game


def clear_widgets():
    widgets = window.grid_slaves()
    for widget in widgets:
        widget.destroy()

def in_game_menu():
    clear_widgets()

    # Show text
    label1 = Label(window, text="Game code: " + game.get_id())
    label2 = Label(window, text=f"{game.get_players_num()}/4 players are connected\n Waiting for admin to start")

    label1.grid(row=0, column=0)
    label2.grid(row=1, column=0)



def create_new_room():
    global game
    clear_widgets()
    #msg = msg_code("connect", "new")
    msg = "new"

    # Create game number
    my_socket.send(msg.encode())
    data = (my_socket.recv(1024).decode()).split('|')
    game = get_game()

    # Show text
    in_game_menu()


def join_private_menu():
    pass


def join_random_menu():
    """ asks the server to connect to any room available """
    # sent to server
    global game_status
    code = "random| "
    my_socket.send(code.encode())
    data = (my_socket.recv(1024).decode()).split('|')

    # messagebox.showinfo(title=None, message=(data[0]))
    # If connected successfully
    if data[1] != "Error":
        game_status = "in game"
        in_game_menu(game_code=data[1])
    # If did not find available rooms
    else:
        game_status = "not in game"
        create_new_room()


def change_user_name():
    pass


# Variables
game_status = "Starting"
game = None

# Server settings
SERVER_IP = "192.168.1.106"
SERVER_PORT = 4457
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect((SERVER_IP, SERVER_PORT))

# Window settings
window = Tk()
window.title("Cambio game menu")
window.geometry("300x150")
window.resizable(True, True)
window.iconbitmap('C:/Users/Nir/PycharmProjects/playGround/img/icon.ico')

# Menu settings
my_menu = Menu(window)
window.config(menu=my_menu)
menu_game = Menu(my_menu)
menu_game.add_command(label="New game", command=create_new_room)
menu_game.add_command(label="Join private game", command=join_private_menu)
menu_game.add_command(label="Change user name", command=change_user_name)
menu_game.add_command(label="Quit game", command=window.quit)
my_menu.add_cascade(label="Game", menu=menu_game)

window.mainloop()
