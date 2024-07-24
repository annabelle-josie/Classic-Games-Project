'''docstring here'''
import pygame
import random

class Letter(pygame.sprite.Sprite):
    '''Letters to be displayed to show what has been chosen already'''
    def __init__(self, x, y, text):
        '''docstring here'''
        super().__init__()
        self.position = (x, y)
        self.text = text
        self.history = "not_chosen" # Options will be "not_chosen", "correct", "incorrect"
    
    def draw(self, surface):
        '''Draws the letter with correct color according to history'''
        if self.history=="not_chosen":
            letter_color = "black"
        elif self.history == "correct":
            letter_color = "green"
        elif self.history == "incorrect":
            letter_color = "red"

        letter_font = pygame.font.SysFont('Press_Start_2P', 40)
        letter_display = letter_font.render(self.text, False, letter_color)
        surface.blit(letter_display, self.position)

    def get_rect(self):
        '''Returns a rect of the letter'''
        return pygame.Rect(self.position, (35,40))

    def get_text(self):
        return self.text

    def incorrect(self):
        '''Sets history to incorrect'''
        self.history = "incorrect"

    def correct(self):
        '''Sets history to correct'''
        self.history = "correct"
    
    def been_chosen(self):
        '''Return True if has been chosen in the past'''
        if self.history == "not_chosen":
            return False
        else:
            return True

def chose_word():
    lines = open("src/hangman_words.txt").read().splitlines()
    word = random.choice(lines)
    print(word)
    displayed_word = "_ " * (len(word))
    return word, displayed_word

def reveal_letters(letter, word, displayed_word):
    '''docstring here'''
    displayed_word = displayed_word.split()
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

    in_a_row = 0
    game_over = False
    hangman_count = 0
    word, displayed_word = chose_word()
    letter_list = [Letter(455,285, "A"), Letter(535,285, "B"), Letter(615,285, "C"), Letter(695,285, "D"),
                   Letter(775,285, "E"), Letter(455,345, "F"), Letter(535,345, "G"), Letter(615,345, "H"),
                   Letter(695,345, "I"), Letter(775,345, "J"), Letter(455,405, "K"), Letter(535,405, "L"),
                   Letter(615,405, "M"), Letter(695,405, "N"), Letter(775,405, "O"), Letter(455,465, "P"),
                   Letter(535,465, "Q"), Letter(615,465, "R"), Letter(695,465, "S"), Letter(775,465, "T"),
                   Letter(455,525, "U"), Letter(535,525, "V"), Letter(615,525, "Y"), Letter(695,525, "X"),
                   Letter(775,525, "Y"), Letter(615,585, "Z")]

    while running:
        screen.fill("white")
        background_images = pygame.image.load("src/images/hangman_background.png").convert()
        screen.blit(background_images, (0, 0))

        if "_" not in displayed_word:
                word, displayed_word = chose_word()
                hangman_count = 0
                in_a_row += 1
                letter_list = [Letter(455,285, "A"), Letter(535,285, "B"), Letter(615,285, "C"), Letter(695,285, "D"),
                            Letter(775,285, "E"), Letter(455,345, "F"), Letter(535,345, "G"), Letter(615,345, "H"),
                            Letter(695,345, "I"), Letter(775,345, "J"), Letter(455,405, "K"), Letter(535,405, "L"),
                            Letter(615,405, "M"), Letter(695,405, "N"), Letter(775,405, "O"), Letter(455,465, "P"),
                            Letter(535,465, "Q"), Letter(615,465, "R"), Letter(695,465, "S"), Letter(775,465, "T"),
                            Letter(455,525, "U"), Letter(535,525, "V"), Letter(615,525, "Y"), Letter(695,525, "X"),
                            Letter(775,525, "Y"), Letter(615,585, "Z")]

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_ESCAPE]:
            escape_to_main = True
        mouse_pos = (0,0)
        if not game_over:
            trigger_reveal = -1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.KEYDOWN:
                    # A = 97 Z = 12
                    trigger_reveal = event.key - 97

            for i, letter in enumerate(letter_list):
                if letter.get_rect().collidepoint(mouse_pos):
                    trigger_reveal = i
            if trigger_reveal >= 0:
                if chr(trigger_reveal+97) in word:
                    displayed_word = reveal_letters(chr(trigger_reveal+97), word, displayed_word)
                    letter_list[trigger_reveal].correct()
                else:
                    if hangman_count > 5:
                        game_over = True
                    elif not letter_list[trigger_reveal].been_chosen():
                        hangman_count+=1
                    letter_list[trigger_reveal].incorrect()

        word_font = pygame.font.SysFont('Press_Start_2P', 40)
        word_display = word_font.render(displayed_word, False, "black")
        screen.blit(word_display, (450,125))

        score_font = pygame.font.SysFont('Press_Start_2P', 50)
        score_display = score_font.render(str(in_a_row), False, "black")
        screen.blit(score_display, (165,150))

        hangman_image = pygame.image.load("src/images/hangman_images/"+str(hangman_count)+".png").convert()
        hangman_image = pygame.transform.scale(hangman_image, (350, 400))
        screen.blit(hangman_image, (875, 250))

        for letter in letter_list:
            letter.draw(screen)

        if game_over:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # A = 97 Z = 12
                    if chr(event.key) == ".":
                        game_over = False
                        word, displayed_word = chose_word()
                        hangman_count = 0
                        in_a_row = 0
                        letter_list = [Letter(455,285, "A"), Letter(535,285, "B"), Letter(615,285, "C"), Letter(695,285, "D"),
                                    Letter(775,285, "E"), Letter(455,345, "F"), Letter(535,345, "G"), Letter(615,345, "H"),
                                    Letter(695,345, "I"), Letter(775,345, "J"), Letter(455,405, "K"), Letter(535,405, "L"),
                                    Letter(615,405, "M"), Letter(695,405, "N"), Letter(775,405, "O"), Letter(455,465, "P"),
                                    Letter(535,465, "Q"), Letter(615,465, "R"), Letter(695,465, "S"), Letter(775,465, "T"),
                                    Letter(455,525, "U"), Letter(535,525, "V"), Letter(615,525, "Y"), Letter(695,525, "X"),
                                    Letter(775,525, "Y"), Letter(615,585, "Z")]

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            go_font = pygame.font.SysFont('Press_Start_2P', 40)
            go_surface = go_font.render("GAME OVER", False, "red")
            screen.blit(go_surface, (450,200))

            go_font = pygame.font.SysFont('Press_Start_2P', 20)
            go_text_surface = go_font.render("Press . to restart", False, "red")
            screen.blit(go_text_surface, (50,550))

        pygame.display.flip()
        dt = clock.tick(60) / 1000

        if(escape_to_main or not running):
            running = False
            return(True)
    pygame.quit()

if __name__ == "__main__":
    game_loop()
