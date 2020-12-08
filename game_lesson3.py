# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:00:14 2020

@author: danhhong
"""
import pygame

# window size, title
surface = pygame.display.set_mode((800,400))
pygame.display.set_caption('Draw Circle')

# change background
surface.fill([255,255,255])


# draw circle
# pygame.draw.circle(surface, (r,g,b), (x, y), R, w)
red = 100
green = 10
blue = 10
color = (255,0,0)   # (Red, Green, Blue)
x, y = 110, 110     # start coordinate of circle center
R = 100             # radius
w = 5               # thickness of the circle border

for i in range(0,50):
    pygame.draw.circle(surface, (red+i*3, green+i*3, blue+i), (x+i, y+i), R, w)

# keybaord control

# quit application
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            
    pygame.display.update()
    
pygame.quit()
quit()