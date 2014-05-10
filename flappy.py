"""Another clone of Flappy Bird"""

import pygame, sys, os
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

pipe_vertical_space = 170
pipe_horizontal_space = 300
pipe_number = 3 #number of pipes loaded at a time

pipe_border = 10 #closest a pipe can get to the edge
pipe_width = 26 * sprites.scale_mag
upper_pipe_height = 135 * sprites.scale_mag
lower_pipe_height = 121 * sprites.scale_mag

def load_image_name(file_name):
    return os.path.join(os.getcwd(), 'data', file_name)

def random_pipe_height():
    upper = display_width - ground_height - pipe_border - pipe_vertical_space
    lower = pipe_border
    return randrange(lower, upper)

def pipe_positions(cur_x, rand_pipe_height_val):
    upper_pos = rand_pipe_height_val - upper_pipe_height
    lower_pos = rand_pipe_height_val + pipe_vertical_space
    return (cur_x, upper_pos), (cur_x, lower_pos)
    
def main():
    pygame.init()
    fps_clock = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((display_length, display_width), 0, 32)
    
    ground = pygame.Rect([0, display_width - ground_height], [display_length, ground_height])

    im_set = map(load_image_name, ['frame0.png', 'frame1.png', 'frame2.png'])
    bird = sprites.Bird(im_set, bird_pos, bird_v, bird_a, jump_power)

    lower_pipe_im = load_image_name('lower_pipe.png')
    upper_pipe_im = load_image_name('upper_pipe.png')

    upper_pipes = []
    lower_pipes = []    

    score = 0
    temp_score = True #makes sure when the bird passes a pipe the score does not increment twice

    for x in range(0, pipe_number):        
        init_x_pos = bird_pos[0] + (1 + x) * pipe_horizontal_space
        upper_pipe_pos, lower_pipe_pos = pipe_positions(init_x_pos, random_pipe_height())
        upper_pipes.append(sprites.Pipe(upper_pipe_im, upper_pipe_pos, ((-1) * scroll_speed, 0)))
        lower_pipes.append(sprites.Pipe(lower_pipe_im, lower_pipe_pos, ((-1) * scroll_speed, 0)))

    sprite_list = [bird]
    for u_pipe in upper_pipes:
        sprite_list.append(u_pipe)
    for l_pipe in lower_pipes:
        sprite_list.append(l_pipe)

    all_sprites = pygame.sprite.RenderPlain(sprite_list)


    while True:    
        #Bird update
        if bird.rect.colliderect(ground):
            game_over()
        
        #pipe updates
        for index, u_pipe in enumerate(upper_pipes):
            if bird.rect.colliderect(u_pipe):
                game_over()
            #check if pipes went off screen for upper pipes only!
            if u_pipe.rect[0] + pipe_width< 0:
                temp_score = True
                new_u_pos, new_l_pos = pipe_positions(u_pipe.rect.left + pipe_number * pipe_horizontal_space, random_pipe_height())
                u_pipe.move(new_u_pos)
                lower_pipes[index].move(new_l_pos)
            #score
            if u_pipe.rect.right < bird.rect.left and temp_score == True:
                score += 1
                print score
                temp_score = False
        for l_pipe in lower_pipes:
            if bird.rect.colliderect(l_pipe):                
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
