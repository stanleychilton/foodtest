import pygame, math

pygame.init()

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

screen_size = (500, 500)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Gravity")
screen.fill(white)

pygame.display.flip()

clock = pygame.time.Clock()
fps = 120

x = screen_size[0]//2
y = screen_size[1]//2

speed = 10

running = True

ball_size = 200
pos = (x-(ball_size//2),y-(ball_size//2))
limits = (0,100)


while running:
    pos = (x, y)
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y -= speed
            elif event.key == pygame.K_a:
                x -= speed
            elif event.key == pygame.K_s:
                y += speed
            elif event.key == pygame.K_d:
                x += speed


    possible = (pos, ball_size)
    pygame.draw.rect(screen, black, (0, 700, 1000, 100))
    ball = pygame.draw.circle(screen, black, pos, ball_size, 1)
    pygame.draw.arc(screen, red,ball,0, math.pi/6)
    pygame.draw.polygon(screen, red, possible)

    pygame.display.flip()
    clock.tick(fps)
