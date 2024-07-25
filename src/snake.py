'''docstring here'''
import pygame
import random

class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y, is_head):
        super().__init__()
        self.position = (x,y)
        self.direction = "left"
        self.head = is_head
    
    def draw(self, surface):
         pygame.draw.rect(surface, "green", (self.position[0], self.position[1], 40, 40))
    
    def isHead(self):
        return self.head
    
    def move_left(self):
        if self.direction != "right":
            self.direction = "left"
    
    def move_right(self):
        if self.direction != "left":
            self.direction = "right"
    
    def move_up(self):
        if self.direction != "down":
            self.direction = "up"

    def move_down(self):
        if self.direction != "up":
            self.direction = "down"



def game_loop():
    '''docstring here'''
    screen_width = 1280
    screen_height = 700
    pygame.display.set_caption('Snake')
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    running = True
    escape_to_main = False
    dt = 0

    game_over = False

    while running:
        screen.fill("black")
        # background_images = pygame.image.load("src/images/snake_background.png").convert()
        # screen.blit(background_images, (0, 0))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_ESCAPE]:
            escape_to_main = True
        
        if not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                snake[0].move_left()
            elif keys[pygame.K_w] or keys[pygame.K_UP]:
                snake[0].move_up()
            elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
                snake[0].move_down()
            elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                snake[0].move_right()

        pygame.display.flip()
        dt = clock.tick(60) / 1000

        if(escape_to_main or not running):
            running = False
            return(True)
    pygame.quit()

if __name__ == "__main__":
    game_loop()
