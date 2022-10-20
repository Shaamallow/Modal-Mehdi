# Import the pygame module

import pygame

# Import pygame.locals for easier access to key coordinates

# Updated to conform to flake8 and black standards

from pygame.locals import (

    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,

)


# Initialize pygame

pygame.init()

# Define constants for the screen width and height

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Variable to keep the main loop running
running = True

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():

        if event.type == KEYDOWN:  # Key is pressed

            if event.key == K_ESCAPE:  # Escape key = quit
                running = False

        elif event.type == QUIT:  # Window is closed

            running = False

    #Fill the screen with black
    #Write name of the game in the middle of the screen 'IQ Test
    #create a start button under the name of the game
    #When the start button is pressed, the game starts

    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 36)
    text = font.render("IQ Test", 1, (255, 255, 255))
    textpos = text.get_rect()
    textpos.centerx = screen.get_rect().centerx
    screen.blit(text, textpos)

    start = False

    #create a starting button for the game
    #start is written on the button
    #when the button is pressed, start variable is set to true



    if (not start):

        button = pygame.Rect(300, 400, 200, 50)
        pygame.draw.rect(screen, (255, 255, 255), button)
        font = pygame.font.Font(None, 36)
        text = font.render("Start", 1, (0, 0, 0))
        textpos = text.get_rect()
        textpos.centerx = button.centerx
        textpos.centery = button.centery
        screen.blit(text, textpos)

    pygame.display.flip()
