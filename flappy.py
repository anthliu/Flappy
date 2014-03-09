import pygame, sys
import pygame.locals as py

FPS = 30 #Frames per second
SPD = 5 #Speed of the bird traveling right
ACC = -3 #Acceleration downward
SCL = 4 #how scaled the sprites are

def main():
    pygame.init()
    DISPLAY = pygame.display.set_mode((640, 480), 0, 32)

    sheet = pygame.image.load('sprites.png')
    
    sheet.set_clip(pygame.Rect(264,64,17,12))
    rawBird = sheet.subsurface(sheet.get_clip())
    rawBirdSize = rawBird.get_rect().size
    bird = pygame.transform.scale(rawBird, (rawBirdSize[0] * SCL, rawBirdSize[1] * SCL))

    while True:
        DISPLAY.fill((255,255,255))
        DISPLAY.blit(bird, (0, 0))
        for event in pygame.event.get():
            if event.type == py.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == "__main__":
    main()
