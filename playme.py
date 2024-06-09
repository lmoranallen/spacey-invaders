import pygame
from game_screen.screen import GameScreen

# pygame setup
pygame.init()
# screen = pygame.display.set_mode([1280, 720])
gamescreen = GameScreen()
fps = pygame.time.Clock()
running = True
print(gamescreen.getDetails())

# initial_pos = pygame.Vector2(gamescreen.get_width()/2, gamescreen.get_height()/2)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame

    # RENDER YOUR GAME HERE
    # pygame.draw.circle(gamescreen, "orange", initial_pos, 25)
    # flip() the display to put your work on screen
    

    fps.tick(60)  # limits FPS to 60

pygame.quit()