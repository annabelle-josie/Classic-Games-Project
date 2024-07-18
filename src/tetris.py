import pygame
import random

#TODO: Points system
#TODO: Win/lose
#TODO: Missing the weird shaped one!

class Square(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.position = (x, y)
        self.color = color
        self.set = False #set will decide if it is moving or still

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], 40, 40), 5)
    
    def get_position(self):
        return self.position
    
    def set_position(self, position):
        self.position = position
    
    def drop(self, speed):
        self.position = (self.position[0], self.position[1]+speed)
    
    def move(self, direction):
        self.position = (self.position[0] + direction, self.position[1])
    
    def is_set(self):
        return set
    
    def get_rect(self):
        return(pygame.Rect(self.position, (40,40)))
    
    def lower(self):
        self.position = (self.position[0], self.position[1]+40)

class Shape(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.squares = []
        self.is_set = False

    def draw(self, surface):
        for i in range(len(self.squares)):
            self.squares[i].draw(surface)
    
    def drop(self, speed):
        can_drop = True
        for i in range(len(self.squares)):
            if (self.squares[i].get_position()[1]+40+speed > 670):
                can_drop = False
                self.is_set = True
        if(can_drop):
            for i in range(len(self.squares)):
                self.squares[i].drop(speed)

    def move_left(self):
        can_move = True
        for i in range(len(self.squares)):
            if (self.squares[i].get_position()[0]-40 < 440):
                can_move = False
        if(can_move):
            for i in range(len(self.squares)):
                self.squares[i].move(-40)

    def move_right(self):
        can_move = True
        for i in range(len(self.squares)):
            if (self.squares[i].get_position()[0]+80 > 840):
                can_move = False
        if(can_move):
            for i in range(len(self.squares)):
                self.squares[i].move(40)    

    def get_is_set(self):
        return self.is_set
    
    def make_set(self):
        self.is_set = True
    
    def doesCollide(self, given_rect):
        collides = False
        for i in range(len(self.squares)):
            this_rect = self.squares[i].get_rect()
            if(this_rect.colliderect(given_rect)):
                collides = True
        return collides
    
    def get_squares(self):
        returnVal = []
        for i in range (len(self.squares)):
            returnVal.append(self.squares[i])
        return returnVal
    
    def rotate(self, rotations):
        position = [0,0]
        new_rot = (self.current_rot + 1) % (len(rotations))
        for i in range(len(self.squares)):
            position = list(self.squares[i].get_position())
            position[0] -= rotations[self.current_rot][i][0]
            position[1] -= rotations[self.current_rot][i][1]
            position[0] += rotations[new_rot][i][0]
            position[1] += rotations[new_rot][i][1]
            self.squares[i].set_position(tuple(position))
            
        self.current_rot = (self.current_rot + 1) % (len(rotations)) 

class S_Shape(Shape):
    def __init__(self):
        super().__init__()
        self.squares = (Square(440,30, "#00ff00"), Square(440, 70, "#00ff00"), Square(480,70, "#00ff00"), Square(480,110, "#00ff00"))
        self.rotations = [[(0,0), (0,40), (40,40), (40,80)],[(0,40), (40,0), (40,40), (80,0)]]
        self.current_rot = 0

    def rotate(self):
        super().rotate(self.rotations)

class Line_Shape(Shape):
    def __init__(self):
        super().__init__()
        self.squares = (Square(440,30, "#00ffff"), Square(440, 70, "#00ffff"), Square(440,110, "#00ffff"), Square(440,150, "#00ffff"))
        self.rotations = [[(0,0), (0,40), (0,80), (0,120)],[(0,0), (40,0), (80,0), (120,0)]]
        self.current_rot = 0

    def rotate(self):
        super().rotate(self.rotations)

class Z_Shape(Shape):
    def __init__(self):
        super().__init__()
        self.squares = (Square(480,30, "#ff0000"), Square(440, 70, "#ff0000"), Square(480,70, "#ff0000"), Square(440,110, "#ff0000"))
        self.rotations = [[(40,0), (0,40), (40,40), (0,80)],[(0,0), (40,0), (40,40), (80,40)]]
        self.current_rot = 0

    def rotate(self):
        super().rotate(self.rotations)

class Square_Shape(Shape):
    def __init__(self):
        super().__init__()
        self.squares = (Square(440,30, "#ffff00"), Square(440, 70, "#ffff00"), Square(480,30, "#ffff00"), Square(480,70, "#ffff00"))
        self.rotations = [[(0,0), (0,40), (40,0), (40,40)]]
        self.current_rot = 0

    def rotate(self):
        super().rotate(self.rotations)

class L_Shape(Shape):
    def __init__(self):
        super().__init__()
        self.squares = (Square(440,30, "#ff7f00"), Square(440, 70, "#ff7f00"), Square(440,110, "#ff7f00"), Square(480,110, "#ff7f00"))
        self.rotations = [[(0,0), (0,40), (0,80), (40,80)],[(0,0), (0,40), (40,0), (80,0)],[(0,0), (40,0), (40,40), (40,80)],[(80,0), (80,40), (40,40), (0,40)]]
        self.current_rot = 0

    def rotate(self):
        super().rotate(self.rotations)

class Rev_L_Shape(Shape):
    def __init__(self):
        super().__init__()
        self.squares = (Square(480,30, "#0000ff"), Square(480, 70, "#0000ff"), Square(480,110, "#0000ff"), Square(440,110, "#0000ff"))
        self.rotations = [[(40,0), (40,40), (40,80), (0,80)],[(0,0), (0,40), (40,40), (80,40)],[(0,0), (0,40), (40,0), (80,0)],[(0,0), (40,0), (80,0), (80,40)]]
        self.current_rot = 0

    def rotate(self):
        super().rotate(self.rotations)

def checkrow(row_num, set_squares):
    # 440,30 is top left corner, squares are 40x40
    row_height = (40 * row_num) + 30
    squares_on_row = []
    for i in range(len(set_squares)):
        if(set_squares[i].get_rect().y - row_height < 20 and set_squares[i].get_rect().y - row_height > -20):
            squares_on_row.append(set_squares[i])
    if(len(squares_on_row) == 10):
        print("delete row")
        return True, squares_on_row
    else:
        return False, []

def gameLoop():
    screen_width = 1280
    screen_height = 700
    pygame.display.set_caption('Tetris')
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    running = True
    escape_to_main = False
    dt = 0
    
    current_shape = Line_Shape()
    all_set_squares = []
    shape_types = [S_Shape, Line_Shape, Z_Shape, Square_Shape, L_Shape, Rev_L_Shape]
    # filled = [[0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], 
    # [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], 
    # [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], 
    # [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], 
    # [0,0,0,0,0,0,0,0,0,0]]

    while running:
        screen.fill("black")
        background_images = pygame.image.load("src/images/tetris_background.png").convert()
        screen.blit(background_images, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif (event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_SPACE):
                    current_shape.rotate()
                if(event.key == pygame.K_LEFT):
                    current_shape.move_left()
                    current_shape.drop(-1)
                elif(event.key == pygame.K_RIGHT):
                    current_shape.move_right()
                    current_shape.drop(-1)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_m] or keys[pygame.K_ESCAPE]:
            escape_to_main = True
        if keys[pygame.K_DOWN]:
            current_shape.drop(2)
        
        if(current_shape.get_is_set()):
            squareList = current_shape.get_squares()
            for i in range (len(squareList)):
                all_set_squares.append(squareList[i])
            rand_num = random.randint(0, len(shape_types)-1)
            current_shape = shape_types[rand_num]()
        
        for i in range(len(all_set_squares)):
            if(current_shape.doesCollide(all_set_squares[i].get_rect())):
                current_shape.make_set()
                squareList = current_shape.get_squares()
                for i in range (len(squareList)):
                    all_set_squares.append(squareList[i])
                rand_num = random.randint(0, len(shape_types)-1)
                current_shape = shape_types[rand_num]()

        for i in range(16):
            remove_row, squares_to_remove = checkrow(i, all_set_squares)
            if(remove_row):
                print("removing")
                for i in range(len(squares_to_remove)):
                    all_set_squares.remove(squares_to_remove[i])
                for i in range(len(all_set_squares)):
                   all_set_squares[i].lower()
            
        
        current_shape.draw(screen)
        for i in range(len(all_set_squares)):
            # print(all_set_squares[i])
            all_set_squares[i].draw(screen)

        current_shape.drop(1)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

        if(escape_to_main or not running):
            running = False
            return(True)
    pygame.quit()

if __name__ == "__main__":
    gameLoop()