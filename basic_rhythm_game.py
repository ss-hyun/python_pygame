import pygame
import sys

# basic setting
play = True
display_size = (300, 600)
background_color = (0,0,0)
tick = 1000
dist_per_sec = 300

pygame.init()
background = pygame.display.set_mode(display_size)
pygame.display.set_caption("basic rhythm game")
fps = pygame.time.Clock()

# button setting
button_color = (255,255,255)
button_size = 50
button_loc = ( background.get_size()[0]/2, background.get_size()[1]-button_size-30 )

# move item
move_item_list = []
item_num = 0
delete_item_num = 0
move_item_color = (100,100,100)
speed = dist_per_sec/tick

while play:
    fps.tick(tick)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            move_item_list.append(button_size)
            item_num += 1
            move_item_pos = button_size + 30
        if event.type == pygame.KEYDOWN and len(move_item_list):
            distance = abs(button_loc[1] - move_item_list[0])
            if distance < 3*button_size:
                if distance > 2*button_size:
                    print("miss")
                elif distance > button_size:
                    print("bad")
                elif distance > button_size/2:
                    print("good")
                elif distance > button_size/6:
                    print("great")
                else:
                    print("perfect!")      
                del move_item_list[0]
                item_num -= 1
    
    background.fill((0,0,0))
    pygame.draw.circle(background, button_color, button_loc, button_size)
    for i in range(item_num):
        pygame.draw.circle(background, move_item_color, (button_loc[0],move_item_list[i]), button_size)
        move_item_list[i] += speed
        if(move_item_list[i]>button_loc[1]+button_size):
            delete_item_num += 1
    if delete_item_num:
        print("miss")
        for i in range(delete_item_num):
            del move_item_list[0]
        item_num -= delete_item_num
        delete_item_num = 0
    pygame.display.update()

pygame.quit()