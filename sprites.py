"""Loading the sprites for the flappy bird game"""

import pygame

scale = 4 #how scaled the sprites are

def scale(image, scale):
    size = image.get_rect().size
    return pygame.transform.scale(image, (size[0] * scale, size[1] * scale))

class Pipe(pygame.sprite.Sprite):
    def __init__(self, pipe_name, xy_pair, v_pair):
        pygame.sprite.Sprite.__init__(self)
        self.image = scale(pygame.image.load(pipe_name), scale)
        self.rect = pygame.Rect(xy_pair, self.image.get_rect().size())
        self.move(v_pair)
    def move(v_pair):
        self.velocity = v_pair
    def update():
        self.rect.move(self.velocity[0], self.velocity[1])

class Bird(pygame.sprite.Sprite):
    def __init__(self, frame_names, xy_pair, v_pair, a_pair, j_pair):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for frame in frame_names:
            self.images.append(scale(pygame.image.load(frame), scale))
        self.image = self.images[0]
        self.rect = pygame.Rect(xy_pair, self.image.get_rect().size())
        self.velocity = v_pair
        self.acceleration = a_pair
        self.jump_force = j_pair
    def jump():
        self.velocity = self.jump_force
    def update():
        self.velocity = [self.velocity[0] + self.acceleration[0], self.velocity[1] + self.acceleration[1]]
        self.rect.move(self.velocity[0], self.velocity[1])
