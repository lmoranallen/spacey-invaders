from pygame import display, Vector2, draw, font, time, quit, QUIT, event

from sprites.player import SpaceShip

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 1280
BACKGROUND_COLOR = (68, 0, 19) # dark burgundy
TITLE = "Challenge #65: Space Invaders"
CLOCK = time.Clock()
PLAYING = True

screen = display.set_mode([SCREEN_HEIGHT, SCREEN_WIDTH])

class GameScreen():
    
    def initialiseGame(self, player):
        FONT = font.SysFont("Arial", 16)

        # create the starting assets
        screen.fill(BACKGROUND_COLOR)

        # initial spaceship position
        draw.circle(screen, "orange", player.position, 20)

        # SCORE font
        score_text = FONT.render(f"SCORE: {player.score}",True, (255,255,255))
        screen.blit(score_text, (220,20))

        # LIVES font
        lives_text = FONT.render(f"LIVES: {player.lives}",True, (255,255,255))
        screen.blit(lives_text, (820,20))

        #draw line and spaceship cover
        draw.line(screen, (0,255,0), [0.1*screen.get_width(), screen.get_height()-10], [0.9*screen.get_width(), screen.get_height()-10], 3)
        for i in range(0,4):
            draw.rect(screen, (0,255,0), [0.2*(i+1)*screen.get_width()-40, screen.get_height()-240, 75, 60])

        #draw enemies
        for j in range(0,3):
            for k in range(0,6):
                draw.rect(screen, (76,12,250), [0.14*(k+1)*screen.get_width(), 0.1*j*screen.get_height()+100, 15, 15])


        display.set_caption(TITLE)

    def __init__(self):
        super().__init__()
        font.init()
        PLAYING = True
        player = SpaceShip("orange", screen)
        self.initialiseGame(player)

        

        print("YOUR CHARACTER", player.lives, player.position)

        while PLAYING:

            # pygame.QUIT event means the user clicked X to close your window
            for event_elem in event.get():
                if event_elem.type == QUIT:
                    PLAYING = False

            

            display.flip()
            dt = CLOCK.tick(60)/1000
        quit()

        
    def getDetails(self):
        return display.Info()