'''docstring here'''
import random
import pygame

#TODO: Points system
#TODO: Lose
#TODO: Missing the weird shaped one! and some rotations broken
#TODO: only move down on top

class Square(pygame.sprite.Sprite):
    '''docstring here'''
    def __init__(self, x, y, color):
        '''docstring here'''
        super().__init__()
        self.position = (x, y)
        self.color = color
        self.set = False #set will decide if it is moving or still

    def draw(self, surface):
        '''docstring here'''
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], 40, 40), 5)

    def get_position(self):
        '''docstring here'''
        return self.position

    def set_position(self, position):
        '''docstring here'''
        self.position = position

    def drop(self, speed):
        '''docstring here'''
        self.position = (self.position[0], self.position[1]+speed)

    def move(self, direction):
        '''docstring here'''
        self.position = (self.position[0] + direction, self.position[1])

    def is_set(self):
        '''docstring here'''
        return set

    def get_rect(self):
        '''docstring here'''
        return(pygame.Rect(self.position, (40,40)))

    def lower(self):
        '''docstring here'''
        self.position = (self.position[0], self.position[1]+40)

class Shape(pygame.sprite.Sprite):
    '''docstring here'''
    def __init__(self):
        '''docstring here'''
        super().__init__()
        self.squares = []
        self.is_set = False
        self.current_rot = 0

    def draw(self, surface):
        '''docstring here'''
        for _, square in enumerate(self.squares):
            square.draw(surface)

    def drop(self, speed):
        '''docstring here'''
        can_drop = True
        for _, square in enumerate(self.squares):
            if square.get_position()[1]+40+speed > 670:
                can_drop = False
                self.is_set = True
        if can_drop:
            for _, square in enumerate(self.squares):
                square.drop(speed)

    def move_left(self):
        '''docstring here'''
        can_move = True
        for _, square in enumerate(self.squares):
            if square.get_position()[0]-40 < 440:
                can_move = False
        if can_move:
            for _, square in enumerate(self.squares):
                square.move(-40)

    def move_right(self):
        '''docstring here'''
        can_move = True
        for _, square in enumerate(self.squares):
            if square.get_position()[0]+80 > 840:
                can_move = False
        if can_move:
            for _, square in enumerate(self.squares):
                square.move(40)

    def get_is_set(self):
        '''docstring here'''
        return self.is_set

    def make_set(self):
        '''docstring here'''
        self.is_set = True

    def does_collide(self, given_rect):
        '''docstring here'''
        collides = False
        for _, square in enumerate(self.squares):
            this_rect = square.get_rect()
            if this_rect.colliderect(given_rect):
                collides = True
        return collides

    def get_squares(self):
        '''docstring here'''
        return_val = []
        for _, square in enumerate(self.squares):
            return_val.append(square)
        return return_val

    def rotate(self, rotations):
        '''docstring here'''
        position = [0,0]
        new_rot = (self.current_rot + 1) % (len(rotations))
        for i, square in enumerate(self.squares):
            position = list(square.get_position())
            position[0] -= rotations[self.current_rot][i][0]
            position[1] -= rotations[self.current_rot][i][1]
            position[0] += rotations[new_rot][i][0]
            position[1] += rotations[new_rot][i][1]
            square.set_position(tuple(position))

        self.current_rot = (self.current_rot + 1) % (len(rotations))

class S_Shape(Shape):
    '''docstring here'''
    def __init__(self):
        '''docstring here'''
        super().__init__()
        self.squares = (Square(440,30, "#00ff00"), Square(440, 70, "#00ff00"), Square(480,70, "#00ff00"), Square(480,110, "#00ff00"))
        self.rotations = [
            [(0,0), (0,40), (40,40), (40,80)],
            [(0,40), (40,0), (40,40), (80,0)]
            ]
        self.current_rot = 0

    def rotate(self, rotations=None):
        '''docstring here'''
        super().rotate(self.rotations)

class Line_Shape(Shape):
    '''docstring here'''
    def __init__(self):
        '''docstring here'''
        super().__init__()
        self.squares = (Square(440,30, "#00ffff"), Square(440, 70, "#00ffff"), Square(440,110, "#00ffff"), Square(440,150, "#00ffff"))
        self.rotations = [
            [(0,0), (0,40), (0,80), (0,120)],
            [(0,0), (40,0), (80,0), (120,0)]
            ]
        self.current_rot = 0

    def rotate(self, rotations=None):
        '''docstring here'''
        super().rotate(self.rotations)

class Z_Shape(Shape):
    '''docstring here'''
    def __init__(self):
        '''docstring here'''
        super().__init__()
        self.squares = (Square(480,30, "#ff0000"), Square(440, 70, "#ff0000"), Square(480,70, "#ff0000"), Square(440,110, "#ff0000"))
        self.rotations = [
            [(40,0), (0,40), (40,40), (0,80)],
            [(0,0), (40,0), (40,40), (80,40)]
            ]
        self.current_rot = 0

    def rotate(self, rotations=None):
        '''docstring here'''
        super().rotate(self.rotations)

class Square_Shape(Shape):
    '''docstring here'''
    def __init__(self):
        '''docstring here'''
        super().__init__()
        self.squares = (Square(440,30, "#ffff00"), Square(440, 70, "#ffff00"), Square(480,30, "#ffff00"), Square(480,70, "#ffff00"))
        self.rotations = [[(0,0), (0,40), (40,0), (40,40)]]
        self.current_rot = 0

    def rotate(self, rotations=None):
        '''docstring here'''
        super().rotate(self.rotations)

class L_Shape(Shape):
    '''docstring here'''
    def __init__(self):
        '''docstring here'''
        super().__init__()
        self.squares = (Square(440,30, "#ff7f00"), Square(440, 70, "#ff7f00"), Square(440,110, "#ff7f00"), Square(480,110, "#ff7f00"))
        self.rotations = [
            [(0,0), (0,40), (0,80), (40,80)],
            [(0,0), (0,40), (40,0), (80,0)],
            [(0,0), (40,0), (40,40), (40,80)],
            [(80,0), (80,40), (40,40), (0,40)]
            ]
        self.current_rot = 0

    def rotate(self, rotations=None):
        '''docstring here'''
        super().rotate(self.rotations)

class Rev_L_Shape(Shape):
    '''docstring here'''
    def __init__(self):
        '''docstring here'''
        super().__init__()
        self.squares = (Square(480,30, "#0000ff"), Square(480, 70, "#0000ff"), Square(480,110, "#0000ff"), Square(440,110, "#0000ff"))
        self.rotations = [
            [(40,0), (40,40), (40,80), (0,80)],
            [(0,0), (0,40), (40,40), (80,40)],
            [(0,0), (0,40), (40,0), (80,0)],
            [(0,0), (40,0), (80,0), (80,40)]
            ]
        self.current_rot = 0

    def rotate(self, rotations=None):
        '''docstring here'''
        super().rotate(self.rotations)

def checkrow(row_num, set_squares):
    '''docstring here'''
    # 440,30 is top left corner, squares are 40x40
    game_over = False
    # if row_num == 16:
    #     game_over = True
    row_height = (40 * row_num) + 30
    squares_on_row = []
    for _, square in enumerate(set_squares):
        if square.get_rect().y - row_height < 20 and square.get_rect().y - row_height > -20:
            squares_on_row.append(square)
    if len(squares_on_row) == 10:
        return True, squares_on_row, game_over
    else:
        return False, [], game_over

def game_loop():
    '''docstring here'''
    screen_width = 1280
    screen_height = 700
    pygame.display.set_caption('Tetris')
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    running = True
    escape_to_main = False
    dt = 0
    game_over = False

    current_shape = Line_Shape()
    all_set_squares = []
    shape_types = [S_Shape, Line_Shape, Z_Shape, Square_Shape, L_Shape, Rev_L_Shape]

    while running:
        screen.fill("black")
        background_images = pygame.image.load("src/images/tetris_background.png").convert()
        screen.blit(background_images, (0, 0))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_m] or keys[pygame.K_ESCAPE]:
                escape_to_main = True

        current_shape.draw(screen)
        for _, square in enumerate(all_set_squares):
            square.draw(screen)

        print(game_over)
        if not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        current_shape.rotate()
                    if event.key == pygame.K_LEFT:
                        current_shape.move_left()
                        current_shape.drop(-1)
                    elif event.key == pygame.K_RIGHT:
                        current_shape.move_right()
                        current_shape.drop(-1)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                current_shape.drop(2)

            if current_shape.get_is_set():
                square_list = current_shape.get_squares()
                for _, square in enumerate(square_list):
                    all_set_squares.append(square)
                rand_num = random.randint(0, len(shape_types)-1)
                current_shape = shape_types[rand_num]()

            for i, square in enumerate(all_set_squares):
                if current_shape.does_collide(square.get_rect()):
                    current_shape.make_set()
                    square_list = current_shape.get_squares()
                    for _, square in enumerate(square_list):
                        all_set_squares.append(square)
                        if square.get_position()[1] < 50:
                            game_over = True
                            break
                    if game_over:
                        break
                    rand_num = random.randint(0, len(shape_types)-1)
                    current_shape = shape_types[rand_num]()

            for i in range(16):
                remove_row, squares_to_remove, temp_over = checkrow(i, all_set_squares)
                if temp_over:
                    game_over = True
                if remove_row:
                    for _, square in enumerate(squares_to_remove):
                        all_set_squares.remove(square)
                    for _, square in enumerate(all_set_squares):
                        square.lower()

            current_shape.draw(screen)
            for _, square in enumerate(all_set_squares):
                square.draw(screen)

            current_shape.drop(1)
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                #Reset
                game_over = False
                current_shape = Line_Shape()
                all_set_squares = []
                shape_types = [S_Shape, Line_Shape, Z_Shape, Square_Shape, L_Shape, Rev_L_Shape]


            game_font = pygame.font.SysFont('Press_Start_2P', 40)
            rest_font = pygame.font.SysFont('Press_Start_2P', 20)

            pygame.draw.rect(screen, "white", (450, 250, 375, 150))
            text_surface = game_font.render('Game Over', False, "black")
            screen.blit(text_surface, (465,300))
            text_surface = rest_font.render('Press R to restart', False, "black")
            screen.blit(text_surface, (460,350))

        pygame.display.flip()
        dt = clock.tick(60) / 1000

        if(escape_to_main or not running):
            running = False
            return(True)
    pygame.quit()

if __name__ == "__main__":
    game_loop()
