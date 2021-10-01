# 이 코드는 Flaticon.com의 자료를 사용해 작성되었습니다

import pygame
pygame.init()

# setting
display_size = (600, 430)
fps = pygame.time.Clock()
tick = 60
running = True

background = pygame.display.set_mode(display_size)
pygame.display.set_caption("pygame_image")

image_bg = pygame.image.load("image/background+image.png")
image_basketball = pygame.image.load("image/free-icon-basketball-ball-70678.png")

size_bg_width = image_bg.get_rect().size[0]
size_bg_height = image_bg.get_rect().size[1]

size_basketball_width = image_basketball.get_rect().size[0]
size_basketball_height = image_basketball.get_rect().size[1]

x_pos_basketball = size_bg_width/2 - size_basketball_width/2
y_pos_basketball = size_bg_height/2 - size_basketball_height/2

while running:
    fps.tick(tick)
    
    background.blit(image_bg, (0, 0))
    background.blit(image_basketball, (x_pos_basketball,y_pos_basketball))
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()