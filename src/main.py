import pygame
from brick import gameLoop as breakout
from tetris import gameLoop as tetris

#TODO: Add size toggle

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

        pygame.display.set_caption('Retro Games')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

        pygame.font.init()

        if(current_screen == "welcome"):
            imp = pygame.image.load("src/images/homescreen.png").convert()
            screen.blit(imp, (0, 0))

            start_rect = pygame.Rect(450, 425, 375, 65)
            if(start_rect.collidepoint(mouse_x, mouse_y)):
                current_screen = "game_choice"
        elif(current_screen == "game_choice"):
            imp = pygame.image.load("src/images/game_choice.png").convert()
            screen.blit(imp, (0, 0))

            main_font = pygame.font.SysFont('Press_Start_2P', 25)

            breakout_text = main_font.render('1. Atari Breakout', False, ("white"))
            breakout_text_rect = breakout_text.get_rect()
            breakout_text_rect.move_ip(300,225)
            screen.blit(breakout_text, breakout_text_rect)

            tetris_text = main_font.render('2. Tetris', False, ("white"))
            tetris_text_rect = tetris_text.get_rect()
            tetris_text_rect.move_ip(300,275)
            screen.blit(tetris_text, tetris_text_rect)

            if (breakout_text_rect.collidepoint(mouse_x, mouse_y)):
                escape = False
                while(not escape):
                    escape = breakout()
            elif(tetris_text_rect.collidepoint(mouse_x, mouse_y)):
                escape = False
                while(not escape):
                    escape = tetris()
                    screen = pygame.display.set_mode((1280,700))

        pygame.display.flip()
        dt = clock.tick(60) / 1000

        

    pygame.quit()


if __name__ == '__main__':
    gameLauncher()
