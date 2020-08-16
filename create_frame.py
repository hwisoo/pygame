import pygame

pygame.init()

# Set screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Set title
pygame.display.set_caption("My Pygame")

# Event loop
running = True
while running:
    for event in pygame.event.get(): # Did an event occur
        if event.type == pygame.QUIT: # Did window close event occur
            running = False # game is no longer running

# Game End
pygame.quit()
