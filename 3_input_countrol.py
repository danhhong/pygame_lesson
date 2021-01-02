# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:00:14 2020

@author: danhhong
"""
import pygame

pygame.init()
width, height = 800, 400
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Input Control')
clock = pygame.time.Clock()

# fill background
white = (255, 255, 255)
black = (0, 0, 0)
surface.fill(black)

# image part
image = pygame.image.load(r'image/whitebird.png')
x, y = 100, 50
y_move = 0

game_over = False

while not game_over:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        # input control
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_move = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_move = 5
            
    # display image
    y += y_move
    surface.fill(black)
    surface.blit(image, (x, y))
    
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()