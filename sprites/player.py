from pygame import Surface, Vector2
from pygame.sprite import Sprite

SHIP_HEIGHT = 25
SHIP_WIDTH = 20


class SpaceShip(Sprite):
    def __init__(self, color):
        Sprite.__init__(self)

        self.image = Surface([SHIP_WIDTH, SHIP_HEIGHT])
        self.image.fill(color)

        self.rect = self.image.get_rect()
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
