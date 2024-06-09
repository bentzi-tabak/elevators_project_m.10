import pygame
from enum import Enum
from Building import Building

class STATUS_GAME(Enum):
    START_GAME = 1
    UPDATE_FLOORS_ELEVATOR = 2
    PLAY = 3

BACKGROUND_COLOR = (250, 250, 250)

pygame.init()

NUM_OF_FLOORS = 12
NUM_OF_ELEVATORS = 3
SCREEN_WIDTH = NUM_OF_ELEVATORS * 71 + 200
SCREEN_HEIGHT = NUM_OF_FLOORS * 71

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
screen.fill(BACKGROUND_COLOR)

elevator_image = "elv (1).png"
floor_image = "wall.png"
button_image = "elevator_button (1).png"
sound = "ding.mp3"

building = Building(NUM_OF_FLOORS, NUM_OF_ELEVATORS, floor_image, button_image, elevator_image, sound)

building.draw_building(screen, SCREEN_HEIGHT)

def main_loop():
    run = True
    clock = pygame.time.Clock()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            else:
                building.handle_event(event, screen, SCREEN_HEIGHT)
        building.update_elevators(screen, SCREEN_HEIGHT)
        building.update_floor_timers(screen, SCREEN_HEIGHT)
        clock.tick(150)  
    pygame.quit()

if __name__ == "__main__":
    main_loop()
