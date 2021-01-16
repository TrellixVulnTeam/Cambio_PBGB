import socket
from tkinter import *
import time
import threading
from tkinter import messagebox


def start_game():
    """ When admin starts the game - activate the pygame file """
    pass


def join_private_room():
    """ when player press the connect button in the "connect_to_private_room" menu """
    global input_field
    global game_status

    # sent to server
    code = "join|" + str(input_field.get())
    my_socket.send(code.encode())
    data = (my_socket.recv(1024).decode()).split('|')

    messagebox.showinfo(title=None, message=(data[0]))
    if data[1] != "Error":
        in_game_menu(data[1])
    else:
        game_status = "not in game"

    print(data)


def in_game_menu(game_code):
    """ the menu that shows to which room you are connected to """
    global label1
    global label2
    global label3
    global button
    global game_status

    game_status = "in game"

    clear_widgets()

    # Show text
    label1 = Label(window, text="Game code: " + game_code)
    label2 = Label(window, text=f"{players_num}/4 players are connected\n Waiting for admin to start")
    label3.config(text="Waiting for admin to start")
    label1.grid(row=0, column=0)
    label2.grid(row=1, column=0)
    label3.grid(row=2, column=0)
    update_num_of_player()


def create_new_room():
    """ when client asks to create new room """
    global label1
    global label2
    global button
    global game_status

    game_status = "create room"

    clear_widgets()

    # Create game number
    my_socket.send("new".encode())
    data = (my_socket.recv(1024).decode()).split('|')
    game_code = data[1]
    game_status = "in game"

    # Show text
    label1 = Label(window, text="Game code: " + game_code)
    label2 = Label(window, text=f"{players_num}/4 players are connected")

    button = Button(window, text="Start game!", width=10, height=1, bg="black", fg="white",
                    command=lambda: start_game())
    label1.grid(row=0, column=0)
    label2.grid(row=1, column=0)
    button.grid(row=2, column=1, pady=20)
    update_num_of_player("admin")


def change_user_name():
    global label1
    global input_field
    global button
    global game_status

    game_status = "change name"
    clear_widgets()
    label1 = Label(window, text="User Name:")
    input_field = Entry(window)
    button = Button(window, text="Update Name", width=10, height=1, bg="black", fg="white", command=update_name)

    label1.grid(row=0, column=0)
    input_field.grid(row=0, column=1)
    input_field.insert(0, USER_NAME)
    button.grid(row=2, column=1, pady=20)


def clear_widgets():
    """ Clears all the widgets from the screen """
    global label1
    global label2
    global label3
    global input_field
    global button

    label1.grid_forget()
    label2.grid_forget()
    input_field.delete(0, END)
    input_field.grid_forget()
    button.grid_forget()


def join_private_menu():
    """ The menu where the player insert the private room's id """
    global label1
    global label2
    global input_field
    global button
    global game_status

    game_status = "join room"
    clear_widgets()

    label1 = Label(window, text="Enter game code:")
    button = Button(window, text="Join game!", width=10, height=1, bg="black", fg="white", command=join_private_room)

    label1.grid(row=0, column=0)
    input_field.grid(row=0, column=1)
    button.grid(row=2, column=1, pady=20)


def join_random_menu():
    """ asks the server to connect to any room available """
    # sent to server
    global game_status
    code = "random| "
    my_socket.send(code.encode())
    data = (my_socket.recv(1024).decode()).split('|')

    messagebox.showinfo(title=None, message=(data[0]))
    # If connected successfully
    if data[1] != "Error":
        game_status = "in game"
        in_game_menu(game_code=data[1])
    else:
        game_status = "not in game"


def update_name():
    global USER_NAME
    global input_field
    global saved_data
    if input_field.get():
        USER_NAME = str(input_field.get())
        saved_data = open("saved_data.txt", "w")
        saved_data.write(USER_NAME)
        print(USER_NAME)


def update_num_of_player(player_type="user"):
    """ updates the number of player that are connected to our game """
    global game_status
    global players_num
    global label2

    if game_status == "in game":
        my_socket.send("get_players_num".encode())
        data = (my_socket.recv(1024).decode()).split('|')
        players_num = data[1]
        text = f"{players_num}/4 players are connected"
        label2.config(text=text)
        label2.after(500, update_num_of_player)


# Server settings
SERVER_IP = "192.168.1.106"
SERVER_PORT = 4457
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect((SERVER_IP, SERVER_PORT))

# Variables settings
players_num = 0
game_status = "change name"

# Checks if there is a text file with the name, if not create one
try:
    saved_data = open("saved_data.txt", "r")
    USER_NAME = saved_data.read()
except:
    USER_NAME = "user"
    saved_data = open("saved_data.txt", "w")
    saved_data.write(USER_NAME)

# Window settings
window = Tk()
window.title("Cambio game options")
window.geometry("300x150")
window.resizable(True, True)
window.iconbitmap('C:/Users/Nir/PycharmProjects/playGround/img/icon.ico')

# Creating widgets
label1 = Label(window, text="User Name:")
label2 = Label(window)
label3 = Label(window)
input_field = Entry(window)
button = Button(window, text="Update Name", width=10, height=1, bg="black", fg="white", command=update_name)
my_menu = Menu(window)

# Menu settings
window.config(menu=my_menu)
menu_game = Menu(my_menu)
menu_game.add_command(label="New game", command=create_new_room)
menu_game.add_separator()
menu_game.add_command(label="Join private game", command=join_private_menu)
menu_game.add_separator()
menu_game.add_command(label="Join random game", command=join_random_menu)
menu_game.add_separator()
menu_game.add_command(label="Change user name", command=change_user_name)
menu_game.add_separator()
menu_game.add_command(label="Quit game", command=window.quit)
my_menu.add_cascade(label="Game", menu=menu_game)

# Placing widgets
label1.grid(row=0, column=0)
input_field.grid(row=0, column=1)
input_field.insert(0, USER_NAME)
button.grid(row=2, column=1, pady=20)

# Starting window
window.mainloop()
print("Game ended")
