import pygame

# Cards
CARD_WIDTH = 91
CARD_HEIGHT = 140
#card_location = (SCREEN_WIDTH/2 - 45, SCREEN_HEIGHT/2 - 70)
card_location = (0, 0)


# Setting up the game window
pygame.init()
SCREEN_WIDTH = 1536
SCREEN_HEIGHT = 864
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption('Cambio - card game')

run = True


while run:
    clock.tick(50)

    # Searching for quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    background = pygame.image.load('images/pics/background.jpg')
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    card = pygame.image.load('images/pics/red_back2.png')
    card = pygame.transform.scale(card, (CARD_WIDTH, CARD_HEIGHT))

    window.blit(background, (0, 0))
    window.blit(card, card_location)
    pygame.display.update()
    card_location = (card_location[0] + 10, card_location[1])


pygame.quit()

