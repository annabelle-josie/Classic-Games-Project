import pygame
import random

class Square(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.position = (x, y)
        self.color = "white"
        self.set = False #set will decide if it is moving or still

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], 20, 20))
    
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

class Shape(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.squares = []
        self.color = "pink"
        self.set = False #set will decide if it is moving or still
    
    # def make_s(self):
    #     self.squares = (Square(0,0), Square(0, 20), Square(20,20), Square(20,40))

    def draw(self, surface):
        for i in range(len(self.squares)):
            self.squares[i].draw(surface)
    
    def drop(self, speed):
        for i in range(len(self.squares)):
            self.squares[i].drop(speed)

    def move_left(self):
        for i in range(len(self.squares)):
            self.squares[i].move(-1)    

    def move_right(self):
        for i in range(len(self.squares)):
            self.squares[i].move(1)    

    def is_set(self):
        return set
    
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
            print(rotations[new_rot][i])
            
        self.current_rot = (self.current_rot + 1) % (len(rotations)) 

#TODO: work out rotations for all others (S is only one with correct rots)
class S_Shape(Shape):
    def __init__(self):
        super().__init__()
        self.squares = (Square(0,0), Square(0, 20), Square(20,20), Square(20,40))
        self.rotations = [[(0,0), (0,20), (20,20), (20,40)],[(0,20), (20,0), (20,20), (40,0)]]
        self.current_rot = 0

    def rotate(self):
        super().rotate(self.rotations)

class Line_Shape(Shape):
    def __init__(self):
        super().__init__()
        self.squares = (Square(0,0), Square(0, 20), Square(0,40), Square(0,60))
        self.rotations = [[(0,0), (0,20), (0,40), (0,60)],[(0,0), (20,0), (40,0), (60,0)]]
        self.current_rot = 0

    def rotate(self):
        super().rotate(self.rotations)

class Z_Shape(Shape):
    def __init__(self):
        super().__init__()
        self.squares = (Square(20,0), Square(0, 20), Square(20,20), Square(0,40))
        self.rotations = [[(20,0), (0,20), (20,20), (0,40)],[(0,0), (20,0), (20,20), (40,20)]]
        self.current_rot = 0

    def rotate(self):
        super().rotate(self.rotations)

class Square_Shape(Shape):
    def __init__(self):
        super().__init__()
        self.squares = (Square(0,0), Square(0, 20), Square(20,0), Square(20,20))
        self.rotations = [[(0,0), (0,20), (20,0), (20,20)]]
        self.current_rot = 0

    def rotate(self):
        super().rotate(self.rotations)

class L_Shape(Shape):
    def __init__(self):
        super().__init__()
        print("l")
        self.squares = (Square(0,0), Square(0, 20), Square(0,40), Square(20,40))
        self.rotations = [[(0,0), (0,20), (0,40), (20,40)],[(0,0), (0,20), (20,0), (40,0)],[(0,0), (20,0), (20,20), (20,40)],[(40,0), (40,20), (20,20), (0,20)]]
        self.current_rot = 0

    def rotate(self):
        super().rotate(self.rotations)

class Rev_L_Shape(Shape):
    def __init__(self):
        super().__init__()
        print("rev l")
        self.squares = (Square(20,0), Square(20, 20), Square(20,40), Square(0,40))
        self.rotations = [[(20,0), (20,20), (20,40), (0,40)],[(0,0), (0,20), (20,20), (40,20)],[(0,0), (0,20), (20,0), (40,0)],[(0,0), (20,0), (40,0), (40,20)]]
        self.current_rot = 0

    def rotate(self):
        super().rotate(self.rotations)

def gameLoop():
    screen_width = 350
    screen_height = 700
    mini = 1 # 0.5 if mini
    pygame.init()
    screen = pygame.display.set_mode((screen_width * mini, screen_height * mini))
    clock = pygame.time.Clock()
    running = True
    escape_to_main = False
    dt = 0
    
    current_shape = L_Shape()
    all_set_shapes = []
    #shape_types = [S_Shape, Line_Shape, Z_Shape, Square_Shape, L_Shape, Rev_L_Shape]
    shape_types = [Square_Shape, Line_Shape]

    while running:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                current_shape.rotate()
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_p):
                all_set_shapes.append(current_shape)
                rand_num = random.randint(0, len(shape_types)-1)
                current_shape = shape_types[rand_num]()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_m] or keys[pygame.K_ESCAPE]:
            escape_to_main = True
        if keys[pygame.K_RIGHT]:
            current_shape.move_right()
            current_shape.drop(-1)
        elif keys[pygame.K_LEFT]:
            current_shape.move_left()
            current_shape.drop(-1)
        elif keys[pygame.K_DOWN]:
            current_shape.drop(2)
        
        current_shape.drop(1)
        current_shape.draw(screen)
        for i in range(len(all_set_shapes)):
            all_set_shapes[i].draw(screen)
        # all_set_shapes = []
        # for i in range(len(all_set_shapes)):
        #     if(current_shape.colliderect(all_set_shapes[i])):
        #         current_shape.make_set()
        #         all_set_shapes.append(current_shape)
        #         random.randint(1, 5)
        #         current_shape = all_set_shapes[i]()
                # Then make a new current_shape

        
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

        if(escape_to_main or not running):
            running = False
            return(True)
    pygame.quit()

if __name__ == "__main__":
    gameLoop()