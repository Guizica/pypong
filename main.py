from settings import *

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720 ))
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            dt = self.clock.tick() / 2
            self.level.run(dt)
            pygame.draw.rect((50,50,50,50))
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()
    
    


