import socket
from tkinter import *
import pickle
from tkinter import messagebox


def start_game():
    pass


def get_game():
    my_socket.send("get_game".encode())
    game = pickle.loads(my_socket.recv(2048))
    return game


def clear_widgets():
    widgets = window.grid_slaves()
    for widget in widgets:
        widget.destroy()


def create_new_room():
    global game
    clear_widgets()

    # Create game number
    my_socket.send("new".encode())
    data = (my_socket.recv(1024).decode()).split('|')
    game_code = data[1]
    game = get_game()

    # Show text
    label1 = Label(window, text="Game code: " + game_code)
    label2 = Label(window, text=f"{game.get_players_num()}/4 players are connected")

    button = Button(window, text="Start game!", width=10, height=1, bg="black", fg="white",
                    command=lambda: start_game())
    label1.grid(row=0, column=0)
    label2.grid(row=1, column=0)
    button.grid(row=2, column=1, pady=20)
    get_game()


def join_private_menu():
    pass


def join_random_menu():
    pass


def change_user_name():
    pass


# Variables
game_status = "Starting"

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
