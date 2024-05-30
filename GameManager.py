import pygame
from Elevator import elevator
from Floor import Floor

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

screen_width = num_of_elevators * 71 + 150
screen_height = num_of_floors * 71
background_color = (250, 250, 250)
screen_size = (screen_width, screen_height)

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
screen.fill((250, 250, 250))
elevator_image = "elv (1).png"
floor_image = "wall.png"
sound = "ding.mp3"

elevators = []
floors = []

for _ in range(num_of_elevators):
    elevators.append(elevator(elevator_image, sound))
for i in range(num_of_elevators):
    elevators[i].draw(i + 1, screen, screen_height, 0)
    pygame.display.flip()
    
for _ in range(num_of_floors):
    floors.append(Floor(floor_image))
for i in range(num_of_floors):
    floors[i].draw(i, screen, screen_height)
    pygame.display.flip()
    
    



        
        
        
                     

#image = pygame.image.load("elv (1).png")
#image_rect = image.get_rect()
run = True
#x = 152
#y = num_of_floors * 71 - 65
#for elevator in range(num_of_elevators):
    #screen.blit(image, (x, y))
    #x += 66
#pygame.display.flip()
 
print(screen)    
    

#screen.blit(image, (150, 30))
#pygame.display.flip()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()