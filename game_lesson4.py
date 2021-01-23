# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:00:14 2020

@author: danhhong
"""
import pygame

# window size, title
surface = pygame.display.set_mode((800,400))
pygame.display.set_caption('Draw Circle')
clock = pygame.time.Clock()

# change background
surface.fill([0,0,255])


# draw circle
# pygame.draw.circle(surface, (r,g,b), (x, y), R, w)
x, y = 100, 100
color = (255,0,0)   # (Red, Green, Blue)
R = 50             # radius
w = 10              # thickness of the circle border

pygame.draw.circle(surface, color, (x,y), R, w)

# keybaord control
y_move = 0

# quit application
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_move = -5
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_move = 5
                
    y += y_move
    surface.fill([0,0,255])
    pygame.draw.circle(surface, color, (x,y), R, w)
    
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
quit()