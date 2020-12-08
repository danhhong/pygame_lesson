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
surface.fill([0,0,255])


# draw circle
# pygame.draw.circle(surface, (r,g,b), (x, y), R, w)
color = (255,0,0)   # (Red, Green, Blue)
center = (150,150)  # coordinate of circle center
R = 100             # radius
w = 20              # thickness of the circle border

pygame.draw.circle(surface, color, center, R, w)

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