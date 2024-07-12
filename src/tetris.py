import pygame
import random

#TODO: Add detection for base of game
#TODO: Empty row when full (so inc detection for full row)
#TODO: Points system
#TODO: Top banner for displaying points
#TODO: Maybe use image for the squares so that bevel is used (depends on which era of tetris aiming for)

class Square(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.position = (x, y)
        self.set = False #set will decide if it is moving or still

    def draw(self, surface, color):
        pygame.draw.rect(surface, color, (self.position[0], self.position[1], 20, 20))
    
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
        return(pygame.Rect(self.position, (20,20)))

class Shape(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.squares = []
        self.color = color
        self.is_set = False #set will decide if it is moving or still
    
    # def make_s(self):
    #     self.squares = (Square(0,0), Square(0, 20), Square(20,20), Square(20,40))

    def draw(self, surface):
        for i in range(len(self.squares)):
            self.squares[i].draw(surface, self.color)
    
    def drop(self, speed):
        for i in range(len(self.squares)):
            self.squares[i].drop(speed)

    def move_left(self):
        for i in range(len(self.squares)):
            self.squares[i].move(-20)    

    def move_right(self):
        for i in range(len(self.squares)):
            self.squares[i].move(20)    

    def get_is_set(self):
        return set
    
    def make_set(self):
        self.is_set = True
    
    def doesCollide(self, list_of_rects):
        collides = False
        for i in range(len(self.squares)):
            for j in range(len(list_of_rects)):
                this_rect = self.squares[i].get_rect()
                if(this_rect.colliderect(list_of_rects[j])):
                    collides = True
        return collides
    
    def get_rects(self):
        rect_list = []
        for i in range(len(self.squares)):
            rect_list.append(self.squares[i].get_rect())
        return rect_list
    
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

#TODO: work out rotations for all others (S is only one with correct rots)
class S_Shape(Shape):
    def __init__(self):
        super().__init__("pink")
        self.squares = (Square(0,0), Square(0, 20), Square(20,20), Square(20,40))
        self.rotations = [[(0,0), (0,20), (20,20), (20,40)],[(0,20), (20,0), (20,20), (40,0)]]
        self.current_rot = 0

    def rotate(self):
        super().rotate(self.rotations)

class Line_Shape(Shape):
    def __init__(self):
        super().__init__("blue")
        self.squares = (Square(0,0), Square(0, 20), Square(0,40), Square(0,60))
        self.rotations = [[(0,0), (0,20), (0,40), (0,60)],[(0,0), (20,0), (40,0), (60,0)]]
        self.current_rot = 0

    def rotate(self):
        super().rotate(self.rotations)

class Z_Shape(Shape):
    def __init__(self):
        super().__init__("white")
        self.squares = (Square(20,0), Square(0, 20), Square(20,20), Square(0,40))
        self.rotations = [[(20,0), (0,20), (20,20), (0,40)],[(0,0), (20,0), (20,20), (40,20)]]
        self.current_rot = 0

    def rotate(self):
        super().rotate(self.rotations)

class Square_Shape(Shape):
    def __init__(self):
        super().__init__("red")
        self.squares = (Square(0,0), Square(0, 20), Square(20,0), Square(20,20))
        self.rotations = [[(0,0), (0,20), (20,0), (20,20)]]
        self.current_rot = 0

    def rotate(self):
        super().rotate(self.rotations)

class L_Shape(Shape):
    def __init__(self):
        super().__init__("yellow")
        self.squares = (Square(0,0), Square(0, 20), Square(0,40), Square(20,40))
        self.rotations = [[(0,0), (0,20), (0,40), (20,40)],[(0,0), (0,20), (20,0), (40,0)],[(0,0), (20,0), (20,20), (20,40)],[(40,0), (40,20), (20,20), (0,20)]]
        self.current_rot = 0

    def rotate(self):
        super().rotate(self.rotations)

class Rev_L_Shape(Shape):
    def __init__(self):
        super().__init__("orange")
        self.squares = (Square(20,0), Square(20, 20), Square(20,40), Square(0,40))
        self.rotations = [[(20,0), (20,20), (20,40), (0,40)],[(0,0), (0,20), (20,20), (40,20)],[(0,0), (0,20), (20,0), (40,0)],[(0,0), (20,0), (40,0), (40,20)]]
        self.current_rot = 0

    def rotate(self):
        super().rotate(self.rotations)

def gameLoop():
    screen_width = 350
    screen_height = 500
    pygame.display.set_caption('Tetris')
    mini = 1 #0.5 if mini
    pygame.init()
    screen = pygame.display.set_mode((screen_width * mini, screen_height * mini))
    clock = pygame.time.Clock()
    running = True
    escape_to_main = False
    dt = 0
    
    current_shape = L_Shape()
    all_set_shapes = []
    shape_types = [S_Shape, Line_Shape, Z_Shape, Square_Shape, L_Shape, Rev_L_Shape]

    while running:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif (event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_SPACE):
                    current_shape.rotate()
                if(event.key == pygame.K_p):
                    all_set_shapes.append(current_shape)
                    rand_num = random.randint(0, len(shape_types)-1)
                    current_shape = shape_types[rand_num]()
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
            current_shape.drop(4)
        
        
        current_shape.draw(screen)
        for i in range(len(all_set_shapes)):
            all_set_shapes[i].draw(screen)
        
        for i in range(len(all_set_shapes)):
            if(current_shape.doesCollide(all_set_shapes[i].get_rects())):
                current_shape.make_set()
                all_set_shapes.append(current_shape)
                rand_num = random.randint(0, len(shape_types)-1)
                current_shape = shape_types[rand_num]()

        current_shape.drop(2)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

        if(escape_to_main or not running):
            running = False
            return(True)
    pygame.quit()

if __name__ == "__main__":
    gameLoop()