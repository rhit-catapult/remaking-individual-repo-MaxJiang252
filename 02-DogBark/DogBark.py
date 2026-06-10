import os
import sys

import pygame


def main():
    # pre-define RGB colors for Pygame
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30

    # initialize the pygame module
    pygame.init()

    # prepare the window (screen)
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption("Text, Sound, and an Image")

    # Prepare the image
    # Use the script's folder so the image can be found even when the program
    # is launched from a different working directory.
    image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "2dogs.JPG")
    dog_image = pygame.image.load(image_path)
    # TODO 3: Scale the image to be the size (IMAGE_SIZE, IMAGE_SIZE)
    dog_image = pygame.transform.scale(dog_image, (IMAGE_SIZE, IMAGE_SIZE))

    # Prepare the text caption(s)
    # TODO 4: Create a font object with a size 28 font.
    font = pygame.font.SysFont("arial", 28)

    # TODO 5: Render the text "Two Dogs" using the font object (it's like MAKING an image).
    caption_1 = font.render("Two Dogs", True, BLACK)
    # Prepare the music
    # TODO 8: Create a Sound object from the "bark.wav" file.
    bark_sound = pygame.mixer.Sound("02-DogBark/bark.wav")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # TODO 9: Play the music (bark) if there's a mouse click.
            if event.type == pygame.MOUSEBUTTONDOWN:
                bark_sound.play()
        # Clear the screen and set the screen background
        screen.fill(WHITE)

        # Draw the image onto the screen
        # TODO 2: Draw the image onto the screen at position (0, 0)
        screen.blit(dog_image, (0, 0))

        # Draw the text onto the screen
        # TODO 6: Draw the text image onto the screen in the middle bottom.
        # Hint: Commands like these might be useful..
        #          screen.get_width(), caption1.get_width(), image1.get_height()
        x_position = screen.get_width() // 2 - caption_1.get_width() // 2
        y_position = IMAGE_SIZE - caption_1.get_height() - 8
        screen.blit(caption_1, (x_position, y_position))
        # TODO 7: On your own, create a new bigger font and in white text place a 'funny' message on top of the image.

        # Update the screen
        pygame.display.update()


main()
