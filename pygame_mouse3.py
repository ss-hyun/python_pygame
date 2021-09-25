import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))

x_pos = 0
y_pos = 0


play = True
draw = False
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = True
            if event.button == 1:
              x_pos, y_pos = pygame.mouse.get_pos()
              pygame.draw.circle(background, (255,0,255), (x_pos, y_pos), 10)
        if event.type == pygame.MOUSEMOTION:
            if draw:
              x_pos, y_pos = pygame.mouse.get_pos()
              pygame.draw.circle(background, (255,0,255), (x_pos, y_pos), 10)
        if event.type == pygame.MOUSEBUTTONUP:
            draw = False
    
    pygame.display.update()

pygame.quit()