from pygame import display, Vector2, draw, font

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 1280
BACKGROUND_COLOR = (68, 0, 19) # dark burgundy
TITLE = "Challenge #65: Space Invaders"

class GameScreen():
    def __init__(self):
        super().__init__()
        font.init()
        FONT = font.SysFont("Arial", 16)
        screen = display.set_mode([SCREEN_HEIGHT, SCREEN_WIDTH])

        
        screen.fill(BACKGROUND_COLOR)
        initial_pos = Vector2(screen.get_width()/2, screen.get_height()-60)
        draw.circle(screen, "orange", initial_pos, 20)

        score_text = FONT.render("SCORE",True, (255,255,255))
        screen.blit(score_text, (220,20))

        lives_text = FONT.render("LIVES",True, (255,255,255))
        screen.blit(lives_text, (820,20))

        

        draw.line(screen, (0,255,0), [0.1*screen.get_width(), screen.get_height()-10], [0.9*screen.get_width(), screen.get_height()-10], 3)
        for i in range(0,4):
            draw.rect(screen, (0,255,0), [0.2*(i+1)*screen.get_width()-40, screen.get_height()-240, 75, 60])

        for j in range(0,3):
            for k in range(0,6):
                draw.rect(screen, (76,12,250), [0.14*(k+1)*screen.get_width(), 0.1*j*screen.get_height()+100, 15, 15])


        display.set_caption(TITLE)
        display.flip()
        
    def getDetails(self):
        return display.Info()