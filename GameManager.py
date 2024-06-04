import pygame
from enum import Enum

from Elevator import elevator
from Floor import Floor


class STATUS_GAME(Enum):
    START_GAME = 1
    UPDATE_FLOORS_ELEVATOR = 2
    PLAY = 3

MARGIN = 80


pygame.init()

def get_an_int(prompt):
    while True:
        try:
            number = int(input(prompt))
            break
        except ValueError:
            print("please a int num")
    return number        



num_of_floors = get_an_int("Please enter the number of floors requested: ")
num_of_elevators = get_an_int("Please enter the number of elevators requested: ")

screen_width = num_of_elevators * 71 + 200
screen_height = num_of_floors * 71
background_color = (250, 250, 250)
screen_size = (screen_width, screen_height)
black_space = 7

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
screen.fill(background_color)
elevator_image = "elv (1).png"
floor_image = "wall.png"
button_image = "elevator_button (1).png"
sound = "ding.mp3"

elevators = pygame.sprite.Group()
floors = []



for _ in range(num_of_floors):
    floors.append(Floor(floor_image, button_image))
for i in range(num_of_floors):
    floors[i].draw(i, screen, screen_height)
 

floor_width = floors[0].image.get_width()

for i in range(num_of_elevators):
    new_elevator = elevator(i, elevator_image, sound)
    elevators.add(new_elevator)
    new_elevator.draw(i + 1, screen, screen_height, floor_width, MARGIN)
# elevators.update()
# elevators.draw(screen)
    pygame.display.flip() 
for elevator in elevators:
    print(elevator.get_rect())
    


    

    
    

    
    

run = True
    
i = 0
print(screen)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if 94 < mouse_pos[0] < 128 :
                print((screen_height - mouse_pos[1]) // 71)
    elevators.update()
    
pygame.quit()