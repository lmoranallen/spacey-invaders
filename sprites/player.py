from pygame import Surface, Vector2, key, K_LEFT, K_RIGHT
from pygame.sprite import Sprite

SHIP_HEIGHT = 25
SHIP_WIDTH = 20


class SpaceShip(Sprite):
    def __init__(self, color, screen):
        Sprite.__init__(self)

        self.image = Surface([SHIP_WIDTH, SHIP_HEIGHT])
        self.image.fill(color)
        self.lives = 3
        self.score = 0
        self.position = Vector2(screen.get_width()/2, screen.get_height()-60)

        self.rect = self.image.get_rect()
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def getLives(self):
        return self.lives
    
    def moveSpaceship(self, screen):
        keys_pressed = key.get_pressed()

        if (keys_pressed[K_LEFT] and self.position.x > 0.1*screen.get_width()):
            self.position.x -= 10

        if (keys_pressed[K_RIGHT] and self.position.x < 0.9*screen.get_width()):
            self.position.x += 10
        
        # screen.blit(self.image, self.position)
        




    
