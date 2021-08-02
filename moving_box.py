import pygame as game 
import sys
import random
import time
import webcolors
import scipy

from pygame.ftfont import SysFont

from scipy.spatial import KDTree
from webcolors import (CSS3_HEX_TO_NAMES,
                        hex_to_rgb)

class Window:

    # Window attributes
    black = (0, 0, 0)
    blue = (0, 191, 255)
    white = (255, 255, 255)

    screen_width = 1000
    screen_height = 800

    screen_max_width = screen_width - 20    
    screen_min_width = screen_width - screen_width

    screen_max_height = screen_height - 20
    screen_min_height = screen_height - screen_height

    x_origin = int(screen_width / 2)
    y_origin = int(screen_height / 2)

    x_direction = int(screen_width / 2)
    y_direction = int(screen_height / 2)
    velocity = 2

    screen  = game.display.set_mode((screen_width, screen_height))
    bg_colour = black

    iterator = 0
    num_shapes = 3 

    start_time = time.time()
    start_text = "Start Game: Press Y to start"
    initial_text = "Hi" 

    initial_time = 10
    current_time = 0
    compared_time = 0
    countdown_time = initial_time

    score = 0
    score_deduct_time = time.time()

    stage_count = 0
    level_count = 1
    level_it = 1
    level_time = 0
    level_time_compare = 5
    level_text_col = white
    level_monitor = 1

    # Function to map rgb values to the closest colour names
    def convert_rgb_to_names(self, rgb_tuple):
    
        # a dictionary of all the hex and their respective names in css3
        css3_db = CSS3_HEX_TO_NAMES
        names = []
        rgb_values = []
        for color_hex, color_name in css3_db.items():
            names.append(color_name)
            rgb_values.append(hex_to_rgb(color_hex))
        
        kdt_db = KDTree(rgb_values)
        distance, index = kdt_db.query(rgb_tuple)
        return f'{names[index]}'

    # Initialises pygame
    def pygame_init(self):
        game.init()

    # Creates the main surface
    def window_create(self):

        self.pygame_init()

        game.display.set_caption('box game')
        self.screen.fill(self.bg_colour)
        game.display.flip()

        self.initial_text = self.start_text

        self.random_gen()

    # Creates the player shape
    def shape_create(self):

        self.random_shapes()  
        game.draw.circle(self.screen, ((self.blue)), (self.x_direction, self.y_direction), 10)  
        game.display.flip()

    #Function to randomly generate the position and colour of 3 squares
    def random_gen(self):
        
        # Global definition of the random x, y and rgb values of the random squares

        global random_x_1, random_y_1, rgb_r_1, rgb_g_1, rgb_b_1, random_x_2, random_y_2, rgb_r_2, rgb_g_2, rgb_b_2
        global random_x_3, random_y_3, rgb_r_3, rgb_g_3, rgb_b_3
    
        random_x_1 = random.randint(box.screen_min_width, box.screen_max_width)
        random_y_1 = random.randint(box.screen_min_height + 50, box.screen_max_height)

        random_x_2 = random.randint(box.screen_min_width, box.screen_max_width)
        random_y_2 = random.randint(box.screen_min_height + 50, box.screen_max_height)

        random_x_3 = random.randint(box.screen_min_width, box.screen_max_width)
        random_y_3 = random.randint(box.screen_min_height + 50, box.screen_max_height)


        rgb_r_1 = random.randint(0, 255)
        rgb_g_1 = random.randint(0, 255)
        rgb_b_1 = random.randint(0, 255)

        rgb_r_2 = random.randint(0, 255)
        rgb_g_2 = random.randint(0, 255)
        rgb_b_2 = random.randint(0, 255)

        rgb_r_3 = random.randint(0, 255)
        rgb_g_3 = random.randint(0, 255)
        rgb_b_3 = random.randint(0, 255)

    # Function to detect collision with the game objects
    def collision_detect(self):

        if self.x_direction > random_x_1 - 10 and self.x_direction < random_x_1 + 30: 
            if self.y_direction > random_y_1 - 10 and self.y_direction < random_y_1 + 30:
                self.countdown_time = self.initial_time
                return 1
        
        if self.x_direction > random_x_2 - 10 and self.x_direction < random_x_2 + 30: 
            if self.y_direction > random_y_2 - 10  and self.y_direction < random_y_2 + 30 :
                return 2
                
        if self.x_direction > random_x_3 - 10  and self.x_direction < random_x_3 + 30 : 
            if self.y_direction > random_y_3 - 10  and self.y_direction < random_y_3 + 30:
                return 3
        
    shape_1_hit_count = 0
    shape_2_hit_count = 0
    shape_3_hit_count = 0

    def random_shapes(self):

        game.draw.rect(self.screen, ((rgb_r_1, rgb_g_1, rgb_b_1)), [random_x_1, random_y_1, 20, 20])
        game.draw.rect(self.screen, ((rgb_r_2, rgb_g_2, rgb_b_2)), [random_x_2, random_y_2, 20, 20])
        game.draw.rect(self.screen, ((rgb_r_3, rgb_g_3, rgb_b_3)), [random_x_3, random_y_3, 20, 20])

        #game.display.flip()

    # Function to iniliase the on-screen text
    def instructions_display_init(self):
        game.font.init()
        instruction_font = game.font.SysFont("Comic Sans", 32)
        instruction_text = instruction_font.render(self.initial_text, True, self.white)
        self.screen.blit(instruction_text, (self.x_origin - int(5 * len(self.initial_text)), self.screen_min_height + 20))
    
    def countdown_display_init(self) :
        game.font.init()    
        instruction_font = game.font.SysFont("Comic Sans", 32)
        instruction_text = instruction_font.render("Time Remaining:  " + str(self.countdown_time), True, self.white)
        self.screen.blit(instruction_text, (self.screen_min_width + 20, self.screen_min_height + 20))
    
    def score_display_init(self) :
        game.font.init()
        instruction_font = game.font.SysFont("Comic Sans", 32)
        instruction_text = instruction_font.render("Score:  " + str(self.score), True, self.white)
        self.screen.blit(instruction_text, (self.screen_min_width + 20, self.screen_min_height + 50))
    
    def level_display_init(self):

        game.font.init()
        level_font = game.font.SysFont("Comic Sans", 32)
        level_text = level_font.render("Level " + str(self.level_count), True, self.level_text_col)
        self.screen.blit(level_text, (self.x_origin, self.y_origin))           
        
    # Function to handle the text displayed
    def instructions_display(self):
        
        name_colour = box.convert_rgb_to_names((rgb_r_1, rgb_g_1, rgb_b_1))
        
        if key.initial_press > 0:
            if self.game_over_display() != 1:
                self.initial_text = "Go to colour " + str(name_colour)
    
    def countdown_display(self):

        if key.initial_press > 0:

            # Detects if time has ticked over a second
            if int(time.time() - self.current_time) != self.compared_time:
                if self.countdown_time == 0:
                    if self.game_over_display() != 1:
                        self.countdown_time = self.initial_time + 1
                
                else:
                    self.countdown_time -= 1
                    self.compared_time += 1
        
    # Function to handle the game over, if the player does not hit the desired square in time, the game will end    
    def game_over_display(self):
        
        if self.collision_detect() != 1 and self.countdown_time == 0:
            self.initial_text = "Game Over, Press R to restart or Q to quit"
            return 1
    
    # Function to to handle score deduction
    def score_deduction(self):
        
        if key.initial_press > 0:
            if float(time.time() - self.score_deduct_time) > 0.8:
                self.score -= 5
                self.score_deduct_time = time.time()
        

    # Function to handle game state when colour is successfully hit
    def colour_hit(self):

        # As we are only tracking object number one, we are only concerned with re-generating the shapes when object 1 is hit
        if self.collision_detect() == 1:
            self.random_gen()
            self.random_shapes()
            self.score += 10
            self.stage_count += 1

            if self.stage_count % 2 == 0 and self.stage_count != 0:
                self.level_count += 1
                self.initial_time -= 1

            # if self.level_monitor != self.level_count:
            #     self.initial_time -= 3
            #     self.level_monitor += 1
        
        # If object 2 or 3 is hit, the game will prompt wrong colour
        if (self.collision_detect() == 2 or self.collision_detect() == 3) and key.initial_press > 0:
            self.initial_text = "Wrong Colour"
            self.score_deduction()
    
    # Function to handle game restart
    def restart_game(self):

        self.initial_text = self.start_text
        key.initial_press = 0
        self.initial_time = 10
        self.x_direction = self.x_origin
        self.y_direction = self.y_origin
        self.countdown_time = self.initial_time
        self.compared_time = 0
        self.level_count = 1    
        self.stage_count = 0
        self.score = 0
        self.random_gen()
        self.random_shapes()
    
    # Function to handle the game loop
    def game_loop(self):
        
        running = True
        while running:
          
            game.time.delay(2)
            key.key_bind()
            for event in game.event.get():

                if event.type == game.QUIT:
                    running = False
                    game.quit()
                    sys.exit()

            box.screen.fill(box.black)
            box.instructions_display_init()
            box.countdown_display_init()
            box.instructions_display()
            box.score_display_init()
            box.level_display_init()
            box.countdown_display()
            key.key_bind()
            box.collision_detect()
            box.colour_hit()
            box.shape_create()

            game.display.flip()
            game.display.update()
             
class Keyboard:

    # Variable will track if 'Y' has has been pressed or not
    initial_press = 0

    # Function to handle the key binds
    def key_bind(self):

        keys = game.key.get_pressed()

        if keys[game.K_a]:
            if self.initial_press != 0 and box.game_over_display() != 1:
                box.x_direction -= box.velocity

        if keys[game.K_d]:
            if self.initial_press != 0 and box.game_over_display() != 1:
                box.x_direction += box.velocity

        if keys[game.K_w]:
            if self.initial_press != 0 and box.game_over_display() != 1:
                box.y_direction -= box.velocity

        if keys[game.K_s]:
            if self.initial_press != 0 and box.game_over_display() != 1:
                box.y_direction += box.velocity

        if keys[game.K_r]:
            box.restart_game()
        
        if keys[game.K_y]:
            self.initial_press += 1
            box.current_time = time.time()
        
        if keys[game.K_q]:
            game.quit()
        
        if box.x_direction > box.screen_max_width :
            box.x_direction =  box.screen_max_width
        
        if box.x_direction < box.screen_min_width :
            box.x_direction =  box.screen_min_width
        
        if box.y_direction > box.screen_max_height :
            box.y_direction =  box.screen_max_height 
        
        if box.y_direction < box.screen_min_height :
            box.y_direction =  box.screen_min_height

# game loop
box = Window()
key = Keyboard()

box.window_create()
box.shape_create()
box.game_loop()