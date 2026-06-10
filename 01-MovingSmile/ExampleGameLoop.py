# The two lines below allow you to use PyGame and System functions.
# Often programmers use code that other developers have written.
import pygame
import sys

# Let's turn pygame ON
pygame.init()

# Let's create a caption for the game window
pygame.display.set_caption("Hello World")
# TODO 00: Change the window caption to say your name.

# Now the screen is where all the magic is going to happen. Our screen will
# have a width of 640 pixels and a height of 480 pixels. The (0,0) point will
# be at the top left of our screen. 
screen = pygame.display.set_mode((640, 480))
# TODO 05: Change the window size, make sure your circle code still works.

# This is a loop that will run forever, simply because True is always true
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Additional interactions with events

    # TODO 01: Make the background white by uncommenting the line below
    screen.fill(pygame.Color("Gray"))

    # Draw things on the screen

    # TODO 02: Try to draw a circle (any size, any color, anywhere)
    pygame.draw.circle(screen, pygame.Color("White"), (screen.get_width() // 2  , 300), 50, 0)

    # TODO 03: Try to draw a red circle in the middle of the screen with a radius 100
    pygame.draw.circle(screen, pygame.Color("Red"), (screen.get_width() // 2, screen.get_height() // 2), 100, 0)

    # TODO 04: Try to draw a yellow circle with the center exactly in the lower left corner of the screen, radius 10
    pygame.draw.circle(screen, pygame.Color(255, 255, 0), (120, 470), 10, 0)

    # This will make sure that things appear on our screen, without this
    # update, everything we do will not be visible!
    # notice how this statement is still inside of the first while loop, but
    # outside of the for loop (why? because it is at the same level of
    # indentation as the for loop statement).
    pygame.display.update()
