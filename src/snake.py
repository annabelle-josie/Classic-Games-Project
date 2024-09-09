'''Snake - incomplete
To be run within the classic games project or individually
'''
import pygame

class Snake(pygame.sprite.Sprite):
    '''Snake Class
    Each block has position and an indication of its movement
    '''
    def __init__(self, x, y, is_head, name):
        '''x, y positions of top left corner of scale
        is_head: shows if the scale is the head of the snake
        direction: shows the current direction the scale is travelling in
        name: purely for testing
        '''
        super().__init__()
        self.position = (x,y)
        self.head = is_head
        self.direction = "up"
        self.name = name

    def draw(self, surface):
        '''docstring here'''
        pygame.draw.rect(surface, "green", (self.position[0], self.position[1], 40, 40))

    def get_name(self):
        '''docstring here'''
        return self.name

    def get_direction(self):
        '''docstring here'''
        return self.direction

    def is_head(self):
        '''docstring here'''
        return self.head

    def update(self, direct):
        '''Updates the position based on the direction given (direct)'''
        if direct == "right":
            velocity = (50,0)
        elif direct == "left":
            velocity = (-50,0)
        elif direct == "up":
            velocity = (0,-50)
        elif direct == "down":
            velocity = (0,50)
        else:
            print("broken")
        self.position = (self.position[0] + velocity[0], self.position[1] + velocity[1])

    def move_left(self):
        '''docstring here'''
        if self.direction != "right":
            self.direction = "left"

    def move_right(self):
        '''docstring here'''
        if self.direction != "left":
            self.direction = "right"

    def move_up(self):
        '''docstring here'''
        if self.direction != "down":
            self.direction = "up"

    def move_down(self):
        '''docstring here'''
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
    snake = [Snake(400,400, True, "head"), Snake(400,450, True, "shoulders"), Snake(400,500, True, "knees"), Snake(400,550, True, "toes")]
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
                        # current_directions.append("left")
                        snake[0].move_left()
                    elif event.key == pygame.K_w or event.key == pygame.K_UP:
                        # current_directions.append("up")
                        snake[0].move_up()
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        # current_directions.append("down")
                        snake[0].move_down()
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        # current_directions.append("right")
                        snake[0].move_right()

        # Update the movement
        current_directions.append(snake[0].get_direction())
        for i, scale in enumerate(snake):
            scale.update(current_directions[len(current_directions) - 1 - i])
            scale.draw(screen)
        print(current_directions)
        pygame.display.flip()
        clock.tick(4)

        if(escape_to_main or not running):
            running = False
            return(True)
    pygame.quit()
    return(False)

if __name__ == "__main__":
    game_loop()
