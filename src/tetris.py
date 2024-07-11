import pygame

class square(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.position = (x, y)
        self.set = False #set will decide if it is moving or still
    
    def is_set(self):
        return set

class shape(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.squares = []
        self.color = "pink"
        self.set = False #set will decide if it is moving or still
    def make_s(self):
        squares.append(Square(0,0), Square(0, 20), Square(20,20))
    
    def is_set(self):
        return set


def gameloop():
    screen_width = 350
    screen_height = 700
    mini = 1 # 0.5 if mini
    pygame.init()
    screen = pygame.display.set_mode((screen_width * mini, screen_height * mini))
    clock = pygame.time.Clock()
    running = True
    escape_to_main = False
    dt = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    pygame.quit()

if __name__ == "__main__":
    gameloop()