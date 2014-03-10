"""Another clone of Flappy Bird"""

import pygame, sys
import pygame.locals as py
from random import randrange
from sprites import *

FPS = 30 #Frames per second
display_length = 640
display_width = 480

bird_speed = 5
acceleration = -2 #Acceleration downward
jump_power = 20

ground_height = 80
bird_x = 40
pipe_verticle_space = 100
pipe_horizontal_space = 200
pipe_number = 3 #number of pipes loaded at a time

upper_pipe_size = upper_pipe.get_rect().size
lower_pipe_size = lower_pipe.get_rect().size

def main():
    pygame.init()
    fps_clock = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((display_length, display_width), 0, 32)
    
    bird_height = 100
    bird_fall = 0
    ground_y = 480 - ground_height

    

    while True:
        #Bird update
        if bird_height >= ground_y:
            bird_fall = 0
            bird_height = ground_y
        elif bird_height < ground_y:
            bird_fall += acceleration

        for event in pygame.event.get():
            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    bird_fall = jump_power
            if event.type == py.QUIT:
                pygame.quit()
                sys.exit()

        bird_height -= bird_fall

        DISPLAY.fill((255,255,255))
        DISPLAY.blit(bird, (bird_x, bird_height))
        
        pygame.display.update()
        fps_clock.tick(FPS)
        

if __name__ == "__main__":
    main()
