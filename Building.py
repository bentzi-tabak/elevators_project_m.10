import pygame
from collections import deque
from Elevator import Elevator
from Floor import Floor

class Building:
    def __init__(self, num_of_floors, num_of_elevators, floor_image, button_image, elevator_image, sound):
        self.num_of_floors = num_of_floors
        self.num_of_elevators = num_of_elevators
        self.elevator_image = elevator_image
        self.sound = sound
        self.elevators = [Elevator(elevator_image, sound) for _ in range(num_of_elevators)]
        self.floors = [Floor(floor_image, button_image) for _ in range(num_of_floors)]
        self.requests = [False] * num_of_floors  
        self.floor_timers = [0] * num_of_floors  

    def draw_building(self, screen, screen_height):
        for i, floor in enumerate(self.floors):
            floor.draw(i, screen, screen_height)
        floor_width = self.floors[0].image.get_width()
        for i, elevator in enumerate(self.elevators):
            elevator.draw(i + 1, screen, screen_height, floor_width, 80)
        pygame.display.flip()

    def update_elevators(self, screen, screen_height):
        for elevator in self.elevators:
            if elevator.queue:
                first_element = elevator.queue[0]
                if elevator.elevator_move(screen, screen_height, first_element):
                    self.requests[first_element] = False 
                    self.floor_timers[first_element] = 0  
                    self.floors[first_element].set_number_color(screen, screen_height, first_element, (0, 0, 0))  

    def request_elevator(self, floor, screen, screen_height):
        if not self.requests[floor]:
            self.requests[floor] = True
            self.floors[floor].set_number_color(screen, screen_height, floor, (0, 255, 0)) 
            closest_elevator = self.find_closest_elevator(floor, screen_height)
            closest_elevator.queue.append(floor)

    def find_closest_elevator(self, floor, screen_height):
        closest_elevator = None
        min_time = float('inf')
        for elevator in self.elevators:
            time_to_floor = elevator.time_to_floor(floor, screen_height)
            if time_to_floor < min_time:
                min_time = time_to_floor
                closest_elevator = elevator
        self.floor_timers[floor] = min_time  
        return closest_elevator

    def update_floor_timers(self, screen, screen_height):
        for i in range(self.num_of_floors):
            if self.requests[i]:
                self.floor_timers[i] = max(0, self.floor_timers[i] - (0.1 / 15))  
                self.floors[i].display_timer(screen, screen_height, i, self.floor_timers[i])
        pygame.display.flip()

    def handle_event(self, event, screen, screen_height):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if 94 < mouse_pos[0] < 128:
                floor = (screen_height - mouse_pos[1]) // 71
                self.request_elevator(floor, screen, screen_height)
