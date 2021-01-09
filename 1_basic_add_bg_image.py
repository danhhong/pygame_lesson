# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:00:14 2020

@author: danhhong
"""
import pygame

pygame.init()

# variable
width, height = 800, 400
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('My First Game')
clock = pygame.time.Clock()

# background
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

surface.fill(blue)

# add image 
image = pygame.image.load(r'image/whitebird.png')

# main function    
def main():
    
    # add image code
    # coordinate
    x, y = 100, 80 
    # display image method
    surface.blit(image, (x, y))
    # end adding image
    
    # quit game function
    game_over = False
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                
        pygame.display.update()
        clock.tick(60)

main()
    
pygame.quit()