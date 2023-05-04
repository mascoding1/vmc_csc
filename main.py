import pygame

# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((89, 140, 76))

    # Draw a solid blue circle in the center
    surface = pygame.display.set_mode((400,300))
    color = (0, 0, 0, 255)
    pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
    pygame.display.flip()

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
