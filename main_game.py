from Card import Card
import pygame

# Setting up the game window
pygame.init()
screen_width = 1200
screen_height = 700
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Cambio - card game')

# Game Variables
run = True  # Game loop variable
clicked_card = None  # The variable that holds the card that was clicked
clicked = True  # If there is a clicked card or not


# Card stats
card_img = pygame.image.load('images/cards/back.png')
card = Card(13, "Spikes", "Black")

# The game loop
while run:
    pygame.time.delay(50)

    # Searching for quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    # Checking for a mouse click
    if event.type == pygame.MOUSEBUTTONDOWN and clicked:

        # If there is clicked card --> extra click will change the card position to the new click location
        if clicked_card is not None:
            temp_pos = (pygame.mouse.get_pos()[0] + 1, pygame.mouse.get_pos()[1] + 1)
            clicked_card.set_pos(temp_pos)
            clicked_card = None


        if card.is_card_location_pressed(pygame.mouse.get_pos()) and clicked_card is None:
            clicked_card = card
        clicked = False


    # for preventing long clicking
    if event.type == pygame.MOUSEBUTTONUP:
        clicked = True


    # Checks if there is a Clicked card and the flip the card (visualu only)
    if clicked_card is not None:
        card_img = pygame.image.load('images/cards/sk.png')
    else:
        card_img = pygame.image.load('images/cards/back.png')


    window.fill((0, 0, 0))
    window.blit(card_img, (card.get_pos()))
    pygame.display.update()

pygame.quit()  # Kill Game
