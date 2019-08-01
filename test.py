import math, pygame, random

pygame.init()

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

colour_list = []

screen_size = (500, 500)

x = screen_size[0]//2.5
y = screen_size[1]//2.5

ball_size = 25
pos = (x,y)
seg_size = 200

running = True

clock = pygame.time.Clock()
fps = 120

user_choice = 5 #int(input(">>"))

while len(colour_list) != user_choice:
    cur_colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    if cur_colour not in colour_list:
        colour_list.append(cur_colour)


screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("food-test")
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
    fill_arc((x, y), seg_size, temp, seg_angle+temp, colour_list[i])
    temp += seg_angle
pygame.draw.circle(screen, white, pos, ball_size)

pygame.mouse.set_pos(pos)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    movement = pygame.mouse.get_pos()
    movement = (movement[0]-x, movement[1]-y)

    if((-seg_size, -seg_size) < movement < (seg_size, seg_size)):
        print(movement)





    pygame.display.flip()
    clock.tick(fps)
