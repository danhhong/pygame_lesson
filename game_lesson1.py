# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 15:48:31 2020
filename: game_lesson1.py
pip3 install pygame
@author: danhhong
"""
import pygame

# window size, title
surface = pygame.display.set_mode((800,400))
pygame.display.set_caption('My First Game')

# change background
surface.fill([0,100,255])

# display text
pygame.font.init()
myfont = pygame.font.SysFont('Arial Black', 40)

# color (Red, Green, Blue)
# Red: 0 -> 255
# Green:  0 -> 255
# Blue:  0 -> 255
textsurface = myfont.render('Hello World!', False, (255,255,255))
surface.blit(textsurface, (10,10))

# quit application
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            
    pygame.display.update()
    
pygame.quit()
quit()