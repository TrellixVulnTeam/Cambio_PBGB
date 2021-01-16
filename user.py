from tkinter import *
from tkinter import messagebox
import random


def start_game():
    pass


def create_new_game():
    # print("New game")
    global label1
    global label2
    global button

    clear_widgets()

    # Create game number
    game_code = str(random.randint(10000000, 99999999))

    # Show text
    label1 = Label(window, text="Game code: " + game_code)
    label2 = Label(window, text=f"{players_num}/4 players are connected")

    button = Button(window, text="Start game!", width=10, height=1, bg="black", fg="white",
                    command=lambda: start_game())
    label1.grid(row=0, column=0)
    label2.grid(row=1, column=0)
    button.grid(row=2, column=1, pady=20)


def change_user_name():
    global label1
    global input_field
    global button

    clear_widgets()
    label1 = Label(window, text="User Name:")
    input_field = Entry(window)
    button = Button(window, text="Update Name", width=10, height=1, bg="black", fg="white", command=update_name)

    label1.grid(row=0, column=0)
    input_field.grid(row=0, column=1)
    input_field.insert(0, USER_NAME)
    button.grid(row=2, column=1, pady=20)


def clear_widgets():
    global label1
    global label2
    global input_field
    global button

    label1.grid_forget()
    label2.grid_forget()
    input_field.delete(0, END)
    input_field.grid_forget()
    button.grid_forget()


def join_existing_game():
    global label1
    global label2
    global input_field
    global button
    print("Join")
    clear_widgets()

    label1 = Label(window, text="Enter game code:")
    button = Button(window, text="Join game!", width=10, height=1, bg="black", fg="white", command=lambda: start_game())

    label1.grid(row=0, column=0)
    input_field.grid(row=0, column=1)
    button.grid(row=2, column=1, pady=20)


def update_name():
    global USER_NAME
    global input_field
    global saved_data
    if input_field.get():
        USER_NAME = str(input_field.get())
        saved_data = open("saved_data.txt", "w")
        saved_data.write(USER_NAME)
        print(USER_NAME)


# Variables settings
players_num = 0

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
input_field = Entry(window)
button = Button(window, text="Update Name", width=10, height=1, bg="black", fg="white", command=update_name)
my_menu = Menu(window)

# Menu settings
window.config(menu=my_menu)
menu_game = Menu(my_menu)
menu_game.add_command(label="New game", command=create_new_game)
menu_game.add_separator()
menu_game.add_command(label="Join existing game", command=join_existing_game)
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
