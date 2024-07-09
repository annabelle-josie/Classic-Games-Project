import pygame

def collisionDetection(player_x, player_y, ball_x, ball_y, x_change, y_change, bricks, gameOver):
    top_left = (ball_x - 10, ball_y - 10)
    base_right = (ball_x + 10, ball_y + 10)
    
    '''Bounce off edges'''
    if (top_left[1] < 0):
        y_change *= -1
    if(base_right[1] > 720):
        gameOver = True
    if (top_left[0] < 0 or base_right[0] > 1280):
        x_change *= -1


    '''If collide with rectangle'''
    if (base_right[0] > player_x and top_left[0] < (player_x + 120) ):
        if(base_right[1] > player_y and top_left[1] < player_y+20):
            y_change *= -1

            if((base_right[0] - player_x) <40):
                x_change =-3
            elif((base_right[0] - player_x) > 80):
                x_change = 3

    '''If collide with brick'''
    for line in range (len(bricks)):
        for brick in range (len(bricks[line])):
            if (bricks[line][brick] == "."):
                rect_lt = (((1280 / 11 +10)*brick + 20),  (55*line + 50))
                rect_rb = (((1280 / 11 +10)*brick + 20)+100,  (55*line + 50) + 100)

                if (base_right[0] > rect_lt[0] and top_left[0] < rect_rb[0]):
                    if(base_right[1] > rect_lt[1] and top_left[1] < rect_rb[1]):
                        bricks[line][brick] = ""
                        y_change *= -1
                        #x_change /= -3

    return(x_change, y_change, bricks, gameOver)
           
def checkWinner(bricks):
    hasWon = True
    for line in range (len(bricks)):
        for brick in range (len(bricks[line])):
            if (bricks[line][brick] == "."):
                hasWon = False

    return hasWon

def gameLoop():

    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    bricks = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],[".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]
    #bricks = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]


    player_x = screen.get_width() / 2
    player_y = (screen.get_height() / 12)*10

    ball_x = screen.get_width() / 2
    ball_y = 500

    x_change = 3
    y_change = 7

    gameOver = False
    won = False

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
        main_font = pygame.font.SysFont('Engadi-Gentle', 100)
        instrc_font = pygame.font.SysFont('Engadi-Gentle', 25)
        

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        won = checkWinner(bricks)

        if (gameOver):
            screen.fill("white")
            text_surface = main_font.render('Game Over', False, (0, 0, 0))
            screen.blit(text_surface, (350,275))
            text_surface = instrc_font.render('Press R to restart', False, (0, 0, 0))
            screen.blit(text_surface, (500,400))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                #Reset
                bricks = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],[".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]
                player_x = 1280 / 2
                player_y = (720 / 12)*10
                ball_x = 1280/ 2
                ball_y = 500
                x_change = 3
                y_change = 10
                gameOver = False
                won = False
        elif(won):
            screen.fill("pink")
            text_surface = main_font.render('You won!', False, (0, 0, 0))
            screen.blit(text_surface, (350,275))
        else:

            for line in range (len(bricks)):
                for brick in range (len(bricks[line])):
                    if (bricks[line][brick] == "."):
                        pygame.draw.rect(screen, "white", (((1280 / 11 +10)*brick + 20), (55*line + 100), 100, 50))
                
            x_change, y_change, bricks, gameOver = collisionDetection(player_x, player_y,ball_x, ball_y,x_change, y_change, bricks, gameOver)

            '''Update ball'''
            ball_x += x_change
            ball_y += y_change

            pygame.draw.rect(screen, "white", (player_x, player_y, 120, 20))
            
            pygame.draw.circle(screen, "white", (ball_x, ball_y), 20)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                if(not(player_x - 300 * dt < 0)):
                    player_x -= 300 * dt
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                if(not(player_x + 300 * dt > screen.get_width()-120)):
                    player_x += 300 * dt

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == '__main__':
    gameLoop()
    