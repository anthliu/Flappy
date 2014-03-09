import pygame, sys
import pygame.locals as py
from sprites import *

FPS = 30 #Frames per second
bird_speed = 5
acceleration = -3 #Acceleration downward
ground_height = 80

def main():
    pygame.init()
    DISPLAY = pygame.display.set_mode((640, 480), 0, 32)

    while True:
        DISPLAY.fill((255,255,255))
        DISPLAY.blit(bird, (0, 0))
        DISPLAY.blit(upper_pipe, (200, 0))
        DISPLAY.blit(lower_pipe, (400, 0))
        for event in pygame.event.get():
            if event.type == py.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == "__main__":
    main()
