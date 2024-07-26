'''docstring here'''
import pygame
# import random

class Snake(pygame.sprite.Sprite):
    '''Snake Class, each block has position and an indication of its movement'''
    def __init__(self, x, y, is_head):
        '''docstring here'''
        super().__init__()
        self.position = (x,y)
        self.direction = "left"
        self.head = is_head
        self.velocity = (-5,0)

    def draw(self, surface):
        '''docstring here'''
        pygame.draw.rect(surface, "green", (self.position[0], self.position[1], 40, 40))

    def update_head(self):
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])

    def update_body(self, previous_vel):
        '''docstring here'''
        self.position = (self.position[0] + previous_vel[0], self.position[1] + previous_vel[1])

    def is_head(self):
        '''docstring here'''
        return self.head
    
    def get_vel(self):
        '''docstring here'''
        return self.velocity

    def move_left(self):
        '''docstring here'''
        if self.direction != "right":
            self.direction = "left"
            self.velocity = (-5, 0)

    def move_right(self):
        '''docstring here'''
        if self.direction != "left":
            self.direction = "right"
            self.velocity = (5, 0)

    def move_up(self):
        '''docstring here'''
        if self.direction != "down":
            self.direction = "up"
            self.velocity = (0, -5)

    def move_down(self):
        '''docstring here'''
        if self.direction != "up":
            self.direction = "down"
            self.velocity = (0, 5)

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
    snake = [Snake(400,400, True), Snake(400, 450, False)]

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

        for i, piece in enumerate(snake):
            if i == 0:
                piece.update_head()
            else:
                piece.update_body(snake[i-1].get_vel())
            piece.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

        if(escape_to_main or not running):
            running = False
            return(True)
    pygame.quit()

if __name__ == "__main__":
    game_loop()
