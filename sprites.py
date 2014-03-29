"""Loading the sprites for the flappy bird game"""

import pygame

scale = 4 #how scaled the sprites are


sheet = pygame.image.load('sprites.png')
    
sheet.set_clip(pygame.Rect(264,64,17,12))
raw_bird = sheet.subsurface(sheet.get_clip())
raw_bird_size = raw_bird.get_rect().size
bird = pygame.transform.scale(raw_bird, (raw_bird_size[0] * scale, raw_bird_size[1] * scale))

sheet.set_clip(pygame.Rect(302,0,26,135))
raw_upper_pipe = sheet.subsurface(sheet.get_clip())
raw_upper_size = raw_upper_pipe.get_rect().size
upper_pipe = pygame.transform.scale(raw_upper_pipe, (raw_upper_size[0] * scale, raw_upper_size[1] * scale))
    
sheet.set_clip(pygame.Rect(330,0,26,121))
raw_lower_pipe = sheet.subsurface(sheet.get_clip())
raw_lower_size = raw_lower_pipe.get_rect().size
lower_pipe = pygame.transform.scale(raw_lower_pipe, (raw_lower_size[0] * scale, raw_lower_size[1] * scale))
