import pygame

pygame.init()
width, height = 800, 400
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('My First Game')
clock = pygame.time.Clock()

game_over = False

# variable for rectangle
color = (255,0,0) # red
x, y = 200, 100
rect_width, rect_height = 50, 200

# draw rectangle
pygame.draw.rect(surface, color, [x, y, rect_width, rect_height])


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()