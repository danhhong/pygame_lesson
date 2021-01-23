# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:00:14 2020

@author: danhhong
"""
import pygame
import time

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

# prepare for game over function
def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
        elif event.type == pygame.KEYDOWN:
            continue
        
        return event.key
    
    
    return None

def makeTextObjs(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def msgSurface(title, subtitle):
    small_text = pygame.font.Font(None, 20)
    large_text = pygame.font.Font(None, 150)
    
    titleTextSurf, titleTextRect = makeTextObjs(title, large_text)
    titleTextRect.center = width / 2, height / 2
    surface.blit(titleTextSurf, titleTextRect)
    
    typTextSurf, typTextRect = makeTextObjs(subtitle, small_text)
    typTextRect.center = width / 2, ((height / 2) + 100)
    surface.blit(typTextSurf, typTextRect)
    
    pygame.display.update()
    time.sleep(1)
    
    while replay_or_quit() == None:
        clock.tick(1)
        
    main()

# over funcion
def gameOver(title, subtitle):
    msgSurface(title, subtitle)
    
def main():
    x, y = 100, 100
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
        
        # use game over function
        if y > height-40 or y < 0:
            gameOver('Game Over', 'Press any key to continue')
        
        pygame.display.update()
        clock.tick(60)
main()    
pygame.quit()