import pygame

pygame.init()
width, height = 800, 400
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Draw Rectangle')
clock = pygame.time.Clock()

game_over = False

# aviable for rectangle
color = (0, 0, 255) # red
x, y = 100, 50
rect_width, rect_height = 300, 200

# draw rectangle
pygame.draw.rect(surface, color, [x, y, rect_width, rect_height])

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()