import pygame
from datetime import datetime

pygame.init()

# setting
display_size = (480, 360)
tick = 60
speed = 5
running = True

background = pygame.display.set_mode(display_size)
pygame.display.set_caption("pygame_keybord")

fps = pygame.time.Clock()

x_pos = background.get_size()[0]//2 #240
y_pos = background.get_size()[1]//2 #180

to_x = 0
to_y = 0

while running:
    # dilfj;al
    fps.tick(tick)
    # dlijfal;
    for event in pygame.event.get(): # [K_UP,K_DOWN,K_RIGHT]
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_UP:
                to_y += -speed
         if event.key == pygame.K_DOWN:
                to_y += speed
         if event.key == pygame.K_RIGHT:
                to_x += speed
         if event.key == pygame.K_LEFT:
                to_x += -speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                to_y -= -speed
            elif event.key == pygame.K_DOWN:
                to_y -= speed
            elif event.key == pygame.K_RIGHT:
                to_x -= speed
            elif event.key == pygame.K_LEFT:
                to_x -= -speed
        print('hi')
    print("hi")
    # dlifja;l
    # dlifja;lk

    x_pos += to_x
    y_pos += to_y

    background.fill((0,0,0))
    pygame.draw.circle(background, (0,0,255), (x_pos, y_pos), 7)
    pygame.display.update()

pygame.quit()