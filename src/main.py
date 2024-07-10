import pygame
from brick import gameLoop

#TODO: Make game launcher
#TODO: Add size toggle
#TODO: Make it look nice

def gameLauncher():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    current_screen = "welcome"

    while running:
        mouse_x = 0 
        mouse_y = 0

        # set the pygame window name
        pygame.display.set_caption('Retro Games')

        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                #print(f'Mouse clicked at {mouse_x}, {mouse_y}')

        pygame.font.init()

        

        if(current_screen == "welcome"):
            # create a surface object, image is drawn on it.
            imp = pygame.image.load("src/images/homescreen.png").convert()
            
            # Using blit to copy content from one surface to other
            screen.blit(imp, (0, 0))

            #If "Start" button clicked
            if ((mouse_x > 450 and mouse_x < 825) and (mouse_y > 425 and mouse_y < 490)):
                    current_screen = "game_choice"
        elif(current_screen == "game_choice"):
            # create a surface object, image is drawn on it.
            imp = pygame.image.load("src/images/gameChoice.png").convert()
            
            # Using blit to copy content from one surface to other
            screen.blit(imp, (0, 0))

            main_font = pygame.font.SysFont('Press_Start_2P', 25)
            text_surface = main_font.render('1. Atari Breakout', False, ("white"))
            text_rect = text_surface.get_rect()
            text_rect.move_ip(300,225)
            screen.blit(text_surface, text_rect)

            if (text_rect.collidepoint(mouse_x, mouse_y)):
                    current_screen = "welcome"
        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == '__main__':
    gameLauncher()
