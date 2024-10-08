'''Snake - incomplete
To be run within the classic games project or individually
'''

# TODO: Snake Scales can be added most of the time, but often go wrong (about 1 in 5 times)
# TODO: Sides badly detected
# TODO: Game over not triggered for overlap
# TODO: No points system/high score/background like other games
# TODO: Deal with data issue

import random
import pygame

class Snake(pygame.sprite.Sprite):
    '''Snake Class
    Each block has position and an indication of its movement
    '''
    def __init__(self, x, y, is_head):
        '''x, y positions of top left corner of scale
        is_head: shows if the scale is the head of the snake
        direction: shows the current direction the scale is travelling in
        name: purely for testing
        '''
        super().__init__()
        self.position = (x,y)
        self.head = is_head
        self.direction = "up" # Only used by the head

    def draw(self, surface):
        '''Draw the scale onto the surface given'''
        pygame.draw.rect(surface, "green", (self.position[0], self.position[1], 40, 40))

    def get_position(self):
        '''Return top, left (x,y) position of the scale'''
        return self.position

    def get_direction(self):
        '''Get the direction the scale is going (only used for the head scale)'''
        return self.direction

    def is_head(self):
        '''Returns if this scale is the head of the snake'''
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
        self.position = (self.position[0] + velocity[0], self.position[1] + velocity[1])

    def move_left(self):
        '''Changes the current direction of the scale to "left". 
        Warning - does not change the actual position, update must also be run'''
        if self.direction != "right":
            self.direction = "left"

    def move_right(self):
        '''Changes the current direction of the scale to "right". 
        Warning - does not change the actual position, update must also be run'''
        if self.direction != "left":
            self.direction = "right"

    def move_up(self):
        '''Changes the current direction of the scale to "up". 
        Warning - does not change the actual position, update must also be run'''
        if self.direction != "down":
            self.direction = "up"

    def move_down(self):
        '''Changes the current direction of the scale to "down". 
        Warning - does not change the actual position, update must also be run'''
        if self.direction != "up":
            self.direction = "down"

def game_loop():
    '''Main game loop'''
    screen_width = 1280
    screen_height = 700
    pygame.display.set_caption('Snake')
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    running = True
    escape_to_main = False
    snake = [Snake(400,400, True), Snake(400,450, False)]
    current_directions = ["up"]
    food_rect = (random.randint(0, 1230), random.randint(0, 650), 40, 40)
    game_over = False

    while running:
        screen.fill("black")

        # Escape keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_ESCAPE]:
            escape_to_main = True

        food_eaten = False

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
                    elif event.key == pygame.K_l:
                        food_eaten = True

            # Update the movement
            # Use some snazzy data structure here
            current_directions.append(snake[0].get_direction())

            for i, scale in enumerate(snake):
                if scale.is_head():
                    # If it collides with food
                    head_rect = pygame.Rect((scale.get_position()), (40, 40))
                    if head_rect.colliderect(food_rect):
                        food_eaten = True
                    page_rect = pygame.Rect((0,0), (1280, 700))
                    if (not head_rect.colliderect(page_rect)):
                        print("snake escaped!")
                        game_over = True
                scale.update(current_directions[len(current_directions) - 1 - i])                
                scale.draw(screen)

            # Generate food
            if food_eaten:
                direct = current_directions[len(current_directions) - 1 - len(snake)]
                velocity = (0,0)
                if direct == "right":
                    velocity = (-50,0)
                elif direct == "left":
                    velocity = (50,0)
                elif direct == "up":
                    velocity = (0,50)
                elif direct == "down":
                    velocity = (0,-50)
                tail_pos = snake[len(snake)-1].get_position()
                snake.append(Snake(tail_pos[0] + velocity[0], tail_pos[1] + velocity[1], False))
                food_rect = (random.randint(0, 25)*50, random.randint(0, 13)*50, 40, 40)
            pygame.draw.rect(screen, "red", (food_rect))

            
        else:
            main_font = pygame.font.SysFont('Press_Start_2P', 100)
            instrc_font = pygame.font.SysFont('Press_Start_2P', 25)

            screen.fill("white")
            text_surface = main_font.render('Game Over', False, "black")
            screen.blit(text_surface, (200,275))
            text_surface = instrc_font.render('Press R to restart', False, "black")
            screen.blit(text_surface, (350,400))
        pygame.display.flip()
        clock.tick(4)
        if(escape_to_main or not running):
            running = False
            return(True)
    pygame.quit()
    return(False)

if __name__ == "__main__":
    game_loop()
