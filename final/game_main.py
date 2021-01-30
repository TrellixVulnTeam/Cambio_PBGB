import pickle

import pygame

def start_cambio(current_socket):
    # Setting up the game window
    pygame.init()
    screen_width = 1200
    screen_height = 700
    window = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Cambio - card game')

    while True:
        pygame.time.delay(50)
        # Searching for quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Kill Game

        msg = "action" + '|' + "get_game" + '|' + '|'
        current_socket.send(msg.encode())
        my_game = pickle.loads(current_socket.recv(2048))
        print(my_game.get_id())

    pygame.quit()  # Kill Game

