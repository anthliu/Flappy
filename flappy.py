"""Another clone of Flappy Bird"""

import pygame, sys
import pygame.locals as py
from random import randrange
import sprites

FPS = 30 #Frames per second
display_length = 640
display_width = 480

bird_pos = [40, 80]
bird_v = [0, 0]
bird_a = [0, 2] #Acceleration downward
jump_power = [0, -20]
scroll_speed = 5

ground_height = 80

pipe_verticle_space = 100
pipe_horizontal_space = 200
pipe_number = 3 #number of pipes loaded at a time

def main():
    pygame.init()
    fps_clock = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((display_length, display_width), 0, 32)
    
    ground = pygame.Rect([0, display_width - ground_height], [display_length, ground_height])

    im_set = ['frame0.png', 'frame1.png', 'frame2.png']
    bird = sprites.Bird(im_set, bird_pos, bird_v, bird_a, jump_power)

    all_sprites = pygame.sprite.RenderPlain((bird,))

    while True:
        #Bird update
        if bird.rect.colliderect(ground):
            game_over()

        for event in pygame.event.get():
            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    bird.jump()
            if event.type == py.QUIT:
                pygame.quit()
                sys.exit()
        
        all_sprites.update()

        DISPLAY.fill((255,255,255))
    
        all_sprites.draw(DISPLAY)

        pygame.display.update()
        fps_clock.tick(FPS)
        
def game_over():
    print "game over!"
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
