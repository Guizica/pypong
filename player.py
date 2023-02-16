from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos, group):
        super().__init__(group)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200
    