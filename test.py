import math
import pygame
import random
import time

pygame.init()

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

colour_list = []

screen_size = (500, 500)

x = screen_size[0]//2
y = screen_size[1]//2


val = 100
total = 1

running = True

clock = pygame.time.Clock()
fps = 120

user_choice = int(input(">>"))

while len(colour_list) != user_choice:
    cur_colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    if cur_colour not in colour_list:
        colour_list.append(cur_colour)


screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Gravity")
screen.fill(white)

def fill_arc(center, radius, theta0, theta1, color, ndiv=50):
    x0, y0 = center

    dtheta = (theta1 - theta0) / ndiv
    angles = [theta0 + i*dtheta for i in range(ndiv + 1)]

    points = [(x0, y0)] + [(x0 + radius * math.cos(theta), y0 - radius * math.sin(theta)) for theta in angles]

    pygame.draw.polygon(screen, color, points)

seg_angle = 2*math.pi/user_choice
print(colour_list)

print(user_choice)

temp = 0

for i in range(user_choice):
    print(colour_list[i])
    fill_arc((x, y), 200, temp, seg_angle+temp, colour_list[i])
    temp += seg_angle

while running:








    pygame.display.flip()
    time.sleep(3)
    clock.tick(fps)
