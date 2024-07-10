import pygame

#TODO: Add points system
#TODO: Add way of making new levels
#TODO: Make compatable for screen size changes (Add gameloop parameter - size either small/large or number)
#Then replace all width/height values with variables not numbers

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
        self.velocity = (self.velocity[1] * -1, self.velocity[1])
    
    def bounce_y(self):
        self.velocity = (self.velocity[1], self.velocity[1] * -1)
    
    def getPos(self):
        return self.position
    
    def get_rect(self):
        return(pygame.Rect(self.position + (20, 20)))

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.position = (x, y)
    
    def draw(self, surface):
        pygame.draw.rect(surface, "white", (self.position[0], self.position[1], 120, 20))
        
    def move_left(self):
        if(self.position[0]-10 > 0):
            self.position = (self.position[0] - 10, self.position[1])
    
    def move_right(self, screen_width):
        if(self.position[0]+10 < screen_width):
            self.position = (self.position[0] + 10, self.position[1])

    def get_rect(self):
        return(pygame.Rect(self.position + (120, 20)))







def collisionDetection(puck, player, bricks, gameOver):
    '''Bounce off edges'''
    if (puck.getPos()[1] - 10 < 0):
        puck.bounce_y()
    if(puck.getPos()[1] + 10 > 720):
        gameOver = True
        #puck.bounce_y() #Uncomment for debugging!
    if (puck.getPos()[0] - 10 < 0 or puck.getPos()[0] + 10 > 1280):
        puck.bounce_x()


    '''If collide with rectangle'''
    if (pygame.Rect.colliderect(puck.get_rect(), player.get_rect())):
            puck.bounce_y()
            #Uncomment and update this once all else works
            '''
            if((base_right[0] - player_x) <40):
                x_change =-3
            elif((base_right[0] - player_x) > 80):
                x_change = 3
            '''

    '''If collide with brick'''
    for line in range (len(bricks)):
        for brick in range (len(bricks[line])):
            this_brick = bricks[line][brick]
            if (this_brick.isVisible()):
                rect_lt = (((1280 / 11 +10)*brick + 20),  (55*line + 50))
                rect_rb = (((1280 / 11 +10)*brick + 20)+100,  (55*line + 50) + 100)

                if(pygame.Rect.colliderect(puck.get_rect(), this_brick.get_rect())):
                    this_brick.setVisible(False)
                    puck.bounce_y()
                    '''
                    if((base_right[0] - rect_lt[0]) < 10):
                        x_change =-3
                    elif((base_right[0] - player_x) > 90):
                        x_change = 3
                    '''
                
                

    return(gameOver)
           
def checkWinner(bricks):
    hasWon = True
    for line in range (len(bricks)):
        for brick in range (len(bricks[line])):
            if ((bricks[line][brick]).isVisible()):
                hasWon = False

    return hasWon

def gameLoop():

    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    screen_width = 1280
    screen_height = 700

    bricks = []
    for line in range (3):
        bricks.append([])
        for brick in range (10):
            bricks[line].append(Brick(((screen_width / 11 +10)*brick + 20), (55*line + 100)))

    player = Player(screen_width / 2, (screen_height / 12)*10)
    puck = Puck(screen_width / 2, 500, 3, 7)

    gameOver = False
    won = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.font.init()
        main_font = pygame.font.SysFont('Press_Start_2P', 100)
        instrc_font = pygame.font.SysFont('Press_Start_2P', 25)
        
        screen.fill("black")
        won = checkWinner(bricks)

        if (gameOver):
            screen.fill("white")
            text_surface = main_font.render('Game Over', False, "white")
            screen.blit(text_surface, (200,275))
            text_surface = instrc_font.render('Press R to restart', False, "white")
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
        elif(won):
            screen.fill("white")
            text_surface = main_font.render('You won!', False, "white")
            screen.blit(text_surface, (350,275))
        else:
            for line in range (len(bricks)):
                for brick in range (len(bricks[line])):
                    if (bricks[line][brick].isVisible()):
                        bricks[line][brick].draw(screen)
                
            gameOver = collisionDetection(puck, player, bricks, gameOver)

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

    pygame.quit()

if __name__ == '__main__':
    gameLoop()
