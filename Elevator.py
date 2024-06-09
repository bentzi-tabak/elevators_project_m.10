import pygame
from collections import deque

class Elevator:
    def __init__(self, image, sound):
        self.current_floor = 0
        self.sound = pygame.mixer.Sound(sound)
        self.image = pygame.image.load(image)
        self.queue = deque()
        self.current_y = 646
        self.rect = self.image.get_rect()
        self.waiting = False
        self.waiting_start_time = None
        
    def draw(self, num, screen, screen_height, floor_width, margin):
        x = floor_width + margin + (65 * num) - 65
        y = screen_height - 64
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.current_y = self.rect.y
        screen.blit(self.image, (x, y))
        
    def update_rect(self, x, y):
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())
    
    def elevator_move(self, screen, screen_height, dst):
        if self.waiting:
            if pygame.time.get_ticks() - self.waiting_start_time >= 2000:
                self.waiting = False
                return True
            else:
                return False
        
        x = self.rect.x
        target_y = screen_height - (71 * (dst + 1) - 7)
        if self.current_y == target_y:
            self.sound.play()
            self.current_floor = dst
            self.queue.popleft()
            self.waiting = True
            self.waiting_start_time = pygame.time.get_ticks()
            return False
        elif self.current_y > target_y:
            self.current_y -= 1  
        else:
            self.current_y += 1  
        self.update_rect(x, self.current_y)
        pygame.draw.rect(screen, (250, 250, 250), self.rect)
        screen.blit(self.image, self.rect)
        pygame.display.flip()
        return False

    def time_to_floor(self, floor, screen_height):
        current_y = self.rect.y
        target_y = screen_height - (71 * (floor + 1) - 7)
        distance = abs(current_y - target_y)
        travel_time = distance / 142  
        stop_time = 2 * len(self.queue)  
        return travel_time + stop_time

        
                