# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:00:14 2020

@author: danhhong
"""
import pygame

pygame.init()
width, height = 800, 400
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('My First Game')
clock = pygame.time.Clock()

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()