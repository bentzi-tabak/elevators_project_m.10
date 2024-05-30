import pygame

class elevator:
    def __init__(self, image, sound):
        self.current_floor = 0
        self.sound = pygame.mixer.Sound(sound)
        self.image = pygame.image.load(image)
        self.job_finished = None
        
        
        
    def draw(self, num, screen, screen_height, floor):
        image_rect = self.image.get_rect()
        x = 152 + (65 * num) - 65
        y = screen_height - 64 - (floor * 71)
        screen.blit(self.image, (x, y))
        pygame.display.flip()
        
       
        