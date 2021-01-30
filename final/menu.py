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
    msg = msg_code("action", "get_game")
    my_socket.send(msg.encode())
    my_game = pickle.loads(my_socket.recv(2048))
    return my_game


def clear_widgets():
    widgets = window.grid_slaves()
    for widget in widgets:
        widget.destroy()


def in_game_menu():
    # If connected to a game
    if game_status == "in game":
        clear_widgets()
        # Show text
        code_txt = Label(window, text="Game code: " + game.get_id())
        players_txt = Label(window,
                            text=f"{game.get_players_num()}/4 players are connected\n Waiting for admin to start")

        code_txt.grid(row=0, column=0)
        players_txt.grid(row=1, column=0)

        # If the player is the game's master
        if my_socket.getsockname() == game.get_master():
            players_txt.config(text=f"{game.get_players_num()}/4 players are connected")
            button = Button(text="Start game!", width=10, height=1, bg="black", fg="white", command=start_game)
            button.grid(row=2, column=1, pady=20)
        print(game.names)


def refresh_menu():
    """ update game every 0.2 sec  and redraw menu"""
    global game
    global game_status

    if game:
        game = get_game()
        in_game_menu()
    label = Label()
    label.after(500, refresh_menu)


def create_new_room():
    global game
    global game_status
    clear_widgets()
    msg = msg_code("connect", "new", USER_NAME)
    game_status = "in game"

    # Create game number
    my_socket.send(msg.encode())
    data = (my_socket.recv(1024).decode()).split('|')
    game = get_game()


def join_private_menu():
    global game_status
    clear_widgets()
    game_status = "join game"

    game_code_text = Label(window, text="Enter game code:")
    input_field = Entry(window)
    button = Button(window, text="Join game", width=10, height=1, bg="black", fg="white",
                    command=lambda: join_private_room(input_field))

    game_code_text.grid(row=0, column=0)
    input_field.grid(row=0, column=1)
    button.grid(row=2, column=1, pady=20)


def join_private_room(input_field):
    global game_status
    global game

    # sent to server
    code = msg_code("connect", "join", str(input_field.get()), USER_NAME)
    my_socket.send(code.encode())
    data = (my_socket.recv(1024).decode()).split('|')

    messagebox.showinfo(title=None, message=(data[0]))
    # If no errors
    if data[1] != "Error":
        in_game_menu()
        game_status = "in game"
        game = get_game()
    else:
        game_status = "not in game"


def join_random_menu():
    """ asks the server to connect to any room available """
    # sent to server
    global game
    global game_status
    msg = msg_code("connect", "random", USER_NAME)
    my_socket.send(msg.encode())
    data = (my_socket.recv(1024).decode()).split('|')

    # messagebox.showinfo(title=None, message=(data[0]))
    # If connected successfully
    if data[1] != "Error":
        game_status = "in game"
        game = get_game()
        in_game_menu()
    # If did not find available rooms
    else:
        game_status = "not in game"
        create_new_room()


def change_user_name_menu():
    global game_status
    clear_widgets()
    game_status = "change name"

    user_text = Label(window, text="User Name:")
    input_field = Entry(window)
    button = Button(window, text="Update Name", width=10, height=1, bg="black", fg="white",
                    command=lambda: update_name(input_field))

    user_text.grid(row=0, column=0)
    input_field.grid(row=0, column=1)
    input_field.insert(0, USER_NAME)
    button.grid(row=2, column=1, pady=20)


def update_name(input_field):
    global USER_NAME
    if input_field.get():
        USER_NAME = str(input_field.get())
        saved_data = open("saved_data.txt", "w")
        saved_data.write(USER_NAME)
        print(USER_NAME)


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
menu_game.add_command(label="Join random game", command=join_random_menu)
menu_game.add_command(label="Change user name", command=change_user_name_menu)
menu_game.add_command(label="Quit game", command=window.quit)
my_menu.add_cascade(label="Game", menu=menu_game)

# Checks if there is a text file with the name, if not create one
try:
    saved_data = open("saved_data.txt", "r")
    USER_NAME = saved_data.read()
except:
    USER_NAME = "user"
    saved_data = open("saved_data.txt", "w")
    saved_data.write(USER_NAME)

change_user_name_menu()
refresh_menu()
window.mainloop()

print("Game ended")
my_socket.send(msg_code("connect", "Quit").encode())
my_socket.close()
