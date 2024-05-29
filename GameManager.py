import pygame

pygame.init()

def get_an_int(prompt):
    while True:
        try:
            number = int(input(prompt))
            break
        except ValueError:
            print("please a int num")
    return number        


num_of_floors = get_an_int("Please enter the number of floors requested")
num_of_elevators = get_an_int("Please enter the number of elevators requested")

screen_width = int(num_of_elevators * 71 + 150)
screen_height = int(num_of_floors * 71)

screen = pygame.display.set_mode((screen_width, screen_height))

run = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.QUIT()