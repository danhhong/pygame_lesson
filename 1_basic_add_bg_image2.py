# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:00:14 2020

@author: danhhong
"""
import pygame

pygame.init()

# variable
surfaceWidth, surfaceHeight = 800, 400
surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
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
    
    # input control available
    y_move = 0
    
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
        surface.fill(blue)
        surface.blit(image, (x, y))
        
        pygame.display.update()
        clock.tick(60)

main()
    
pygame.quit()