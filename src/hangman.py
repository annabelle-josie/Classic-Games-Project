'''docstring here'''
import pygame

def reveal_letters(letter, word, displayed_word):
    '''docstring here'''
    displayed_word = displayed_word.split()
    print(letter, word, displayed_word)
    for i, w_letter in enumerate(word):
        if w_letter == letter:
            displayed_word[i] = letter
    displayed_word = ' '.join(displayed_word)
    return(displayed_word)

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
    hangman_count = 0
    word = "hello"
    displayed_word = "_ _ _ _ _ "

    while running:
        screen.fill("white")
        background_images = pygame.image.load("src/images/hangman_background.png").convert()
        screen.blit(background_images, (0, 0))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_m] or keys[pygame.K_ESCAPE]:
            escape_to_main = True
        if not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    # A = 97 Z = 122
                    if chr(event.key) in word:
                        displayed_word = reveal_letters(chr(event.key), word, displayed_word)
                    else:
                        if hangman_count > 5:
                            print("agadgafh")
                            game_over = True
                        else:
                            print("pssgas")
                            hangman_count+=1
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            go_font = pygame.font.SysFont('Press_Start_2P', 40)
            go_surface = go_font.render("GAME OVER", False, "red")
            screen.blit(go_surface, (450,125))

        word_font = pygame.font.SysFont('Press_Start_2P', 40)
        word_display = word_font.render(displayed_word, False, "black")
        screen.blit(word_display, (450,125))

        hangman_image = pygame.image.load("src/images/hangman_images/"+str(hangman_count)+".png").convert()
        hangman_image = pygame.transform.scale(hangman_image, (350, 400))
        screen.blit(hangman_image, (875, 250))

        pygame.display.flip()
        dt = clock.tick(60) / 1000

        if(escape_to_main or not running):
            running = False
            return(True)
    pygame.quit()

if __name__ == "__main__":
    game_loop()
