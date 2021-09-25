import pygame
import sys
import os
import random

# basic setting
play = True
display_size = (400, 700)
background_color = (0,0,0)
tick = 1000

pygame.init()
background = pygame.display.set_mode(display_size, pygame.SRCALPHA)
pygame.display.set_caption("simple rhythm game")
fps = pygame.time.Clock()

# item setting
horiz_mid = display_size[0]/2
## game setting box
box_button_num = 3
box_color = (100,100,100)
box_attribute = [0,0,display_size[0],100]
box_button_size = 60
set_button_center = -box_button_size//2
box_button_color = (0,0,0)
box_button_top_loc = 20
box_button_attribute = [
    [horiz_mid - 2*box_button_size + set_button_center, box_button_top_loc, box_button_size, box_button_size],
    [horiz_mid + set_button_center, box_button_top_loc, box_button_size, box_button_size],
    [horiz_mid + 2*box_button_size + set_button_center, box_button_top_loc, box_button_size, box_button_size]
]
font = pygame.font.SysFont(None,20)
text_color = (255,255,255)
box_button_text = [ 
    font.render("start", True, text_color),
    font.render("pause", True, text_color),
    font.render("reset", True, text_color)
]
## button
button_num = 3
button_color = (0,0,255)
button_size = 40
bottom_loc = display_size[1] - button_size - 30
button_loc = [ 
    (horiz_mid - 2*button_size - 30, bottom_loc),
    (horiz_mid , bottom_loc),
    (horiz_mid + 2*button_size + 30 , bottom_loc)
]
font = pygame.font.SysFont(None,50)
text_color = (255,255,255)
button_text = [ 
    font.render("1", True, text_color),
    font.render("2", True, text_color),
    font.render("3", True, text_color)
]
## slide button
dist_per_sec = 350
slide_button_color = (255,0,0)
slide_button_size = 35
top_loc = box_attribute[3] - slide_button_size
start_loc = [ 
    horiz_mid - 2*button_size - 30,
    horiz_mid,
    horiz_mid + 2*button_size + 30
]
class SlideButton:
    speed = dist_per_sec/tick
    def __init__(self):
        self.pos = top_loc
    def move(self):
        self.pos += self.speed
slide_button = [
    [], # button 1 list
    [], # button 2 list
    []  # button 3 list
]

## game state
running = False
tick_count = 0
min_term = 100
max_term = 500

def draw_current_state():
    background.fill(background_color)
    for i in range(button_num):
        pygame.draw.circle(background, button_color, button_loc[i], button_size)
        background.blit(button_text[i], button_loc[i])
    for line in range(button_num):
        for i in range(len(slide_button[line])):
            slide_button[line][i].move()
            pygame.draw.circle(background, slide_button_color, (start_loc[line], slide_button[line][i].pos), slide_button_size)
    pygame.draw.rect(background, box_color, box_attribute, 0)
    for i in range(box_button_num):
        pygame.draw.rect(background, box_button_color, box_button_attribute[i], 0)
        background.blit(box_button_text[i], (box_button_attribute[i][0]+10, box_button_attribute[i][1]+10))
    pygame.display.update()

def click_button(line):
    distance = abs(bottom_loc - slide_button[line][0].pos)
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
        del slide_button[line][0]

# initial background show
draw_current_state()

while play:
    fps.tick(tick)
    
    if running:
        tick_count += 1
        
        # 이전 slide button 생성(or start) 이후 100tick(0.1sec) 이상 지난 경우 0.5%의 확률로 slide button을 생성함
        # 이전 slide button 생성(or start) 이후 500tick(0.5sec) 이상 지난 경우 slide button을 생성함
        if tick_count > min_term and (random.randrange(200) == 100 or tick_count > max_term):
            slide_button[random.randrange(button_num)].append(SlideButton())
            tick_count = 0
    
        # draw and show current state
        draw_current_state()

    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_KP1 or event == pygame.K_1) and len(slide_button[0]):
                click_button(0)
            elif (event.key == pygame.K_KP2 or event == pygame.K_2) and len(slide_button[1]):
                click_button(1)
            elif (event.key == pygame.K_KP3 or event == pygame.K_3) and len(slide_button[2]):
                click_button(2)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            xpos, ypos = pygame.mouse.get_pos()
            # click start button
            if(xpos > box_button_attribute[0][0] and xpos < box_button_attribute[0][0]+box_button_size
            and ypos > box_button_attribute[0][1] and ypos < box_button_attribute[0][1]+box_button_size):
                running = True
            # click pause button
            elif(xpos > box_button_attribute[1][0] and xpos < box_button_attribute[1][0]+box_button_size
            and ypos > box_button_attribute[1][1] and ypos < box_button_attribute[1][1]+box_button_size):
                running = False
            # click reset button
            elif(xpos > box_button_attribute[2][0] and xpos < box_button_attribute[2][0]+box_button_size
            and ypos > box_button_attribute[2][1] and ypos < box_button_attribute[2][1]+box_button_size):
                running = False
                tick = 0
                for line in range(button_num):
                    slide_button[line].clear()
                draw_current_state()
                
        # click quit
        elif event.type == pygame.QUIT:
            play = False
        
        # delete miss slide button
        for line in range(button_num):
            if len(slide_button[line]) and slide_button[line][0].pos > display_size[1] + slide_button_size:
                del slide_button[line][0]
                print("miss")
        


pygame.quit()