import pygame

pygame.init()

# Set screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Set title
pygame.display.set_caption("My Pygame")

# Load background image
background = pygame.image.load("/Users/jamescho/Desktop/pygame/background.png")

# Event loop
running = True
while running:
    for event in pygame.event.get(): # Did an event occur
        if event.type == pygame.QUIT: # Did window close event occur
            running = False # game is no longer running
    screen.blit(background, (0, 0)) # draw background

    pygame.display.update() # refresh display   
# Game End
pygame.quit()
