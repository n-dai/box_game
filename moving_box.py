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

    def pygame_init(self):
        game.init()

    def window_create(self):

        self.pygame_init()

        game.display.set_caption('box game')
        self.screen.fill(self.bg_colour)
        game.display.flip()

        self.initial_text = self.start_text

        self.random_gen()

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

    def collision_detect(self):

        if self.x_direction > random_x_1 - 10 and self.x_direction < random_x_1 + 30: 
            if self.y_direction > random_y_1 - 10 and self.y_direction < random_y_1 + 30:
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

        # if self.collision_detect() == 1: 
        #     game.draw.rect(self.screen, ((self.black)), [random_x_1, random_y_1, 20, 20])
        #     self.shape_1_hit_count += 1

        # if self.collision_detect() == 2:
        #     game.draw.rect(self.screen, ((self.black)), [random_x_2, random_y_2, 20, 20])
        #     self.shape_2_hit_count += 1
        
        # if self.collision_detect() == 3:
        #     game.draw.rect(self.screen, ((self.black)), [random_x_3, random_y_3, 20, 20])
        #     self.shape_3_hit_count += 1

        # if self.shape_1_hit_count > 0:
        #     game.draw.rect(self.screen, ((self.black)), [random_x_1, random_y_1, 20, 20])

        
        # if self.shape_2_hit_count > 0:
        #     game.draw.rect(self.screen, ((self.black)), [random_x_2, random_y_2, 20, 20])

        # if self.shape_3_hit_count > 0:
        #     game.draw.rect(self.screen, ((self.black)), [random_x_3, random_y_3, 20, 20])
    

        game.display.flip()


    def instructions_display_init(self):
        game.font.init()
        instruction_font = game.font.SysFont("Calibri", 32)
        instruction_text = instruction_font.render(self.initial_text, True, self.white)
        self.screen.blit(instruction_text, (self.x_origin - int(6 * len(self.initial_text)), self.screen_min_height + 20))
    
    def instructions_display(self):
        
        name_colour = box.convert_rgb_to_names((rgb_r_1, rgb_g_1, rgb_b_1))

        if key.initial_press > 0:
            self.initial_text = "Go to colour " + str(name_colour)
    
    def colour_hit(self):

        if self.collision_detect() == 1:
            self.random_gen()
            self.random_shapes()
        
        if self.collision_detect() == 2 or self.collision_detect() == 3:
            self.initial_text = "Wrong Colour"
    
    def restart_game(self):

        self.initial_text = self.start_text
        key.initial_press = 0
        self.x_direction = self.x_origin
        self.y_direction = self.y_origin
        self.random_gen()
        self.random_shapes()

    def game_loop(self):
        
        running = True
        while running:
          
            game.time.delay(4)
            key.key_bind()
            for event in game.event.get():

                if event.type == game.QUIT:
                    running = False
                    game.quit()
                    sys.exit()

            box.screen.fill(box.black)
            box.instructions_display_init()
            box.instructions_display()
            key.key_bind()
            self.collision_detect()
            self.colour_hit()
            self.shape_create()

            game.display.flip()
            game.display.update()
             
class Keyboard:

    initial_press = 0

    def key_bind(self):

        keys = game.key.get_pressed()

        if keys[game.K_a]:
            if self.initial_press != 0:
                box.x_direction -= box.velocity

        if keys[game.K_d]:
            if self.initial_press != 0:
                box.x_direction += box.velocity

        if keys[game.K_w]:
            if self.initial_press != 0:
                box.y_direction -= box.velocity

        if keys[game.K_s]:
            if self.initial_press != 0:
                box.y_direction += box.velocity

        if keys[game.K_r]:
            box.restart_game()
        
        if keys[game.K_y]:
            self.initial_press += 1
        
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