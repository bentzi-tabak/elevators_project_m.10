from typing import Any
import pygame

class elevator():
    def __init__(self, id,  image, sound):
        self.id = id
        self.current_floor = 0
        self.sound = pygame.mixer.Sound(sound)
        self.image = pygame.image.load(image)
        self.job_finished = 0
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        
        
        
    def draw(self, num, screen, screen_height, floor_width, margin):
        x = floor_width + margin + (65 * num) - 65
        y = screen_height - 64 
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())
        screen.blit(self.image, (x, y))
        self.position = (x, y)
        
    def get_rect(self):
        return self.rect
    # def update():
              

        
        
       
        