# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:00:14 2020

@author: danhhong
"""
import pygame

pygame.init()
width, height = 800, 400
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Add Image')
clock = pygame.time.Clock()

# fill background
white = (255, 255, 255)
black = (0, 0, 0)
surface.fill(black)

# image part
image = pygame.image.load(r'image/whitebird.png')

game_over = False

while not game_over:
    
    # display image
    surface.blit(image, (100, 50))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()