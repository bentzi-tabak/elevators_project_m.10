import pygame

class Floor:
    def __init__(self, image, button_image):
        self.image = pygame.image.load(image)
        self.button_image = pygame.image.load(button_image)
        
    def draw(self, num, screen, screen_height):
        x = 0
        y = screen_height - 64 - (num * 71)
        screen.blit(self.image, (x, y))
        self.draw_button(screen, y)
        self.draw_black_space(screen, screen_height, num)
        self.draw_floor_number(screen, screen_height, num, (0, 0, 0))
        
    def draw_button(self, screen, y):
        screen.blit(self.button_image, (80, y))
        
    def draw_black_space(self, screen, screen_height, num):
        black_space = pygame.Rect(0, screen_height - (71 * (num + 1)), 129, 7)
        pygame.draw.rect(screen, (0, 0, 0), black_space)
        
    def draw_floor_number(self, screen, screen_height, num, color):
        numbers_font = pygame.font.Font('RubikDoodleShadow-Regular.ttf', 36)
        text = numbers_font.render(f"{num}", True, color)
        screen.blit(text, (45, (screen_height - 55 - (num * 71))))
        
    def set_number_color(self, screen, screen_height, num, color):
        self.draw_floor_number(screen, screen_height, num, color)
        
    def display_timer(self, screen, screen_height, num, time_left):
        x = 130
        y = screen_height - 55 - (num * 71)
        pygame.draw.rect(screen, (250, 250, 250), (x, y, 50, 40))  
        timer_font = pygame.font.Font('RubikDoodleShadow-Regular.ttf', 20)
        text = timer_font.render(f"{time_left:.1f}", True, (255, 0, 0))
        screen.blit(text, (x, y))

        
       