import pygame

class Floor:
    def __init__(self, image, button_image):
        self.image = pygame.image.load(image)
        self.button_image = pygame.image.load(button_image)
        
        
        
        
    def draw(self, num, screen, screen_height):
        x = 0
        y = screen_height - 64 - (num * 71)
        screen.blit(self.image, (x, y))
        screen.blit(self.button_image, (80, y))
        black_space = pygame.Rect(0, screen_height - (71 * (num + 1)), 129, 7)
        pygame.draw.rect(screen, (0, 0, 0), black_space)
        numbers_font = pygame.font.Font('RubikDoodleShadow-Regular.ttf', 36)
        text = numbers_font.render(f"{num}", True, (0, 0, 0))
        screen.blit(text, (45, (screen_height - 55 - (num * 71))))
        # pygame.display.flip()
        
    #def button_position(num):
        
       
        
       