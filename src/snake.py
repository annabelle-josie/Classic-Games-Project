'''Snake - incomplete
To be run within the classic games project or individually
'''
import pygame
# import random

class Snake(pygame.sprite.Sprite):
    '''Snake Class
    Each block has position and an indication of its movement
    '''
    def __init__(self, x, y, is_head, name):
        '''x, y positions of top left corner of block
        is_head: shows if the block is the head of the snake
        name: purely for testing
        '''
        super().__init__()
        self.position = (x,y)
        self.direction = "left"
        # self.pre_direction = "left"
        self.head = is_head
        self.name = name

    def draw(self, surface):
        '''docstring here'''
        pygame.draw.rect(surface, "green", (self.position[0], self.position[1], 20, 20))

    def get_name(self):
        '''docstring here'''
        return self.name

    def get_direction(self):
        '''docstring here'''
        return self.direction

    # def get_pre_dir(self):
    #     '''docstring here'''
    #     return self.pre_direction

    def is_head(self):
        '''docstring here'''
        return self.head

    def update(self, dir):
        if dir == "right":
            velocity = (20,0)
        elif dir == "left":
            velocity = (-20,0)
        elif dir == "up":
            velocity = (0,-20)
        elif dir == "down":
            velocity = (0,20)
        else:
            print("broken")
        self.position = (self.position[0] + velocity[0], self.position[1] + velocity[1])
        print(self.direction)

    def update_head(self):
        '''docstring here'''
        if self.direction == "right":
            velocity = (20,0)
        elif self.direction == "left":
            velocity = (-20,0)
        elif self.direction == "up":
            velocity = (0,-20)
        elif self.direction == "down":
            velocity = (0,20)
        else:
            print("broken")
        self.position = (self.position[0] + velocity[0], self.position[1] + velocity[1])
        print(self.direction)

    # def update_body(self, pre_dir):
    #     '''docstring here'''
    #     if pre_dir == "right":
    #         previous_vel = (20,0)
    #     elif pre_dir == "left":
    #         previous_vel = (-20,0)
    #     elif pre_dir == "up":
    #         previous_vel = (0,-20)
    #     elif pre_dir == "down":
    #         previous_vel = (0,20)
    #     self.position = (self.position[0] + previous_vel[0], self.position[1] + previous_vel[1])

    def move_left(self):
        '''docstring here'''
        if self.direction != "right":
            # self.pre_direction = self.direction
            self.direction = "left"

    def move_right(self):
        '''docstring here'''
        if self.direction != "left":
            # self.pre_direction = self.direction
            self.direction = "right"

    def move_up(self):
        '''docstring here'''
        if self.direction != "down":
            # self.pre_direction = self.direction
            self.direction = "up"

    def move_down(self):
        '''docstring here'''
        if self.direction != "up":
            # self.pre_direction = self.direction
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
    snake = [Snake(400,400, True, "head")]
    current_directions = ["up"]

    game_over = False

    while running:
        screen.fill("black")
        # background_images = pygame.image.load("src/images/snake_background.png").convert()
        # screen.blit(background_images, (0, 0))

        # Escape keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_ESCAPE]:
            escape_to_main = True

        if not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # Arrow key and awsd movement
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        # snake[0].move_left()
                    elif event.key == pygame.K_w or event.key == pygame.K_UP:
                        # snake[0].move_up()
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        # snake[0].move_down()
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        # snake[0].move_right()

        # Update the movement
        for i in range(len(snake)):
            snake[i].update(current_directions[i])
            snake[i].draw(screen)
            # if snake[len(snake)-i-1].is_head():
            #     snake[len(snake)-i-1].update_head()
            # else:
            #     print("something something")
                # snake[len(snake)-i-1].update_body(snake[len(snake)-i-2].get_pre_dir())
            # snake[len(snake)-i-1].draw(screen)

        pygame.display.flip()
        clock.tick(4)

        if(escape_to_main or not running):
            running = False
            return(True)
    pygame.quit()
    return(False)

if __name__ == "__main__":
    game_loop()
