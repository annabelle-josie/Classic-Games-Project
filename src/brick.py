import pygame

#TODO: Potentially add a waiting start button - it starts as soon as loaded atm
#TODO: Add way of making new levels like Mario

class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.position = (x, y)
        self.visible = True
    
    def draw(self, surface):
        pygame.draw.rect(surface, "white", (self.position[0], self.position[1], 100, 50))
        
    def setVisible(self, newValue):
        self.visible = newValue

    def isVisible(self):
        return(self.visible)
    
    def get_rect(self):
        return(pygame.Rect(self.position + (100, 50)))
    
    def get_x(self):
        return(self.position[0])

class Puck(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity_x, velocity_y):
        super().__init__()
        self.position = (x, y)
        self.velocity = (velocity_x, velocity_y)
    
    def update(self):
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])
    
    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, 20)
        
    def bounce_x(self):
        self.velocity = (self.velocity[0] * -1, self.velocity[1])

    def vel_left(self):
        self.velocity = (-3, self.velocity[1])
    
    def vel_right(self):
        self.velocity = (3, self.velocity[1])
    
    def bounce_y(self):
        self.velocity = (self.velocity[0], self.velocity[1] * -1)
    
    def getPos(self):
        return self.position
    
    def get_rect(self):
        return(pygame.Rect(self.position[0]-10, self.position[1]-10, 20, 20))

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.position = (x, y)
    
    def draw(self, surface):
        pygame.draw.rect(surface, "white", (self.position[0], self.position[1], 120, 20))
        
    def move_left(self):
        if(self.position[0] > 0):
            self.position = (self.position[0] - 10, self.position[1])
    
    def move_right(self, screen_width):
        if(self.position[0] < (screen_width-120)):
            self.position = (self.position[0] + 10, self.position[1])

    def get_rect(self):
        return(pygame.Rect(self.position + (120, 20)))
    
    def get_x(self):
        return(self.position[0])

def collisionDetection(puck, player, bricks, gameOver, lives_left, score):
    reset_needed = False
    '''Bounce off edges'''
    if (puck.getPos()[1] - 10 < 100):
        puck.bounce_y()
    if(puck.getPos()[1] + 10 > 720):
        if(lives_left == 1):
            gameOver = True
        else:
            lives_left -= 1
            reset_needed = True
            #puck.bounce_y() #Uncomment for debugging!
    if (puck.getPos()[0] - 10 < 0 or puck.getPos()[0] + 10 > 1280):
        puck.bounce_x()

    '''If collide with rectangle'''
    if (pygame.Rect.colliderect(puck.get_rect(), player.get_rect())):
            puck.bounce_y()
            if(((puck.getPos()[0]+10) - player.get_x()) < 40):
                puck.vel_left()
            elif((puck.getPos()[0]+10 - player.get_x()) > 80):
                puck.vel_right()

    '''If collide with brick'''
    for line in range (len(bricks)):
        for brick in range (len(bricks[line])):
            this_brick = bricks[line][brick]
            if (this_brick.isVisible()):
                if(pygame.Rect.colliderect(puck.get_rect(), this_brick.get_rect())):
                    this_brick.setVisible(False)
                    puck.bounce_y()
                    score += 4
                    if(((puck.getPos()[0]+10) - this_brick.get_x()) <40):
                        puck.vel_left()
                    elif((puck.getPos()[0]+10 - this_brick.get_x()) > 80):
                        puck.vel_right()

    return(gameOver, lives_left, reset_needed, score)
           
def checkWinner(bricks):
    hasWon = True
    for line in range (len(bricks)):
        for brick in range (len(bricks[line])):
            if ((bricks[line][brick]).isVisible()):
                hasWon = False

    return hasWon

def gameLoop():
    #Variables could one day be used to change the size, but lots depend on them secretly, so will take a while
    screen_width = 1280
    screen_height = 700
    pygame.display.set_caption('Breakout')

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    running = True
    escape_to_main = False
    dt = 0

    bricks = []
    for line in range (3):
        bricks.append([])
        for brick in range (10):
            bricks[line].append(Brick(((screen_width / 11 +10)*brick + 20), (55*line + 100)))

    player = Player(screen_width / 2, (screen_height / 12)*10)
    puck = Puck(screen_width / 2, 500, 3, 7)

    gameOver = False
    won = False
    lives_left = 3
    score = 0
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_m] or keys[pygame.K_ESCAPE]:
            escape_to_main = True

        pygame.font.init()
        main_font = pygame.font.SysFont('Press_Start_2P', 100)
        instrc_font = pygame.font.SysFont('Press_Start_2P', 25)
        score_font = pygame.font.SysFont('Press_Start_2P', 50)
        
        screen.fill("black")
        won = checkWinner(bricks)

        header_image = pygame.image.load("src/images/breakout_header.png").convert()
        screen.blit(header_image, (0, 0))

        heart_space = ["", '', '']
        for i in range (lives_left):
            heart_space[i] = pygame.image.load("src/images/life.png").convert()
            screen.blit(heart_space[i], (250 + (100*i), 0))
        
        score_text = score_font.render(str(score), False, "black")
        screen.blit(score_text, (600,25))

        if (gameOver):
            screen.fill("white")
            text_surface = main_font.render('Game Over', False, "black")
            screen.blit(text_surface, (200,275))
            text_surface = instrc_font.render('Press R to restart', False, "black")
            screen.blit(text_surface, (350,400))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                #Reset
                bricks = []
                for line in range (3):
                    bricks.append([])
                    for brick in range (10):
                        bricks[line].append(Brick(((screen_width / 11 +10)*brick + 20), (55*line + 100)))

                player = Player(screen_width / 2, (screen_height / 12)*10)
                puck = Puck(screen_width / 2, 500, 3, 7)
                gameOver = False
                won = False
                lives_left = 3

        elif(won):
            screen.fill("white")
            text_surface = main_font.render('You won!', False, "white")
            screen.blit(text_surface, (350,275))
        else:
            for line in range (len(bricks)):
                for brick in range (len(bricks[line])):
                    if (bricks[line][brick].isVisible()):
                        bricks[line][brick].draw(screen)
                
            gameOver, lives_left, reset_needed, score = collisionDetection(puck, player, bricks, gameOver, lives_left, score)
            if(reset_needed):
                #Reset
                bricks = []
                for line in range (3):
                    bricks.append([])
                    for brick in range (10):
                        bricks[line].append(Brick(((screen_width / 11 +10)*brick + 20), (55*line + 100)))

                player = Player(screen_width / 2, (screen_height / 12)*10)
                puck = Puck(screen_width / 2, 500, 3, 7)
                gameOver = False
                won = False
                reset_needed = False
                
            '''Update ball'''
            puck.update()
            puck.draw(screen)
            player.draw(screen)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                player.move_left()
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                player.move_right(screen_width)

        pygame.display.flip()

        dt = clock.tick(60) / 1000
        if(escape_to_main or not running):
            running = False
            return(True)

    pygame.quit()
    

if __name__ == '__main__':
    gameLoop()
