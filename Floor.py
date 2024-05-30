import pygame

class Floor:
    def __init__(self, image):
        self.image = pygame.image.load(image)
        
        
        
    def draw(self, num, screen, screen_height):
        image_rect = self.image.get_rect()
        x = 0
        y = screen_height - 64 - (num * 71)
        screen.blit(self.image, (x, y))
        rect = pygame.Rect(0, screen_height - (71 * (num + 1)), 129, 7)
        pygame.draw.rect(screen, (0, 0, 0), rect)
        pygame.display.flip()
        
       