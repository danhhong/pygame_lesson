import pygame

pygame.init()
width, height = 800, 400
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('My First Game')
clock = pygame.time.Clock()

game_over = False

#variable for circle
color = (255,0,0) # red
x, y = 100, 150
R = 50
w = 10

# draw circle
pygame.draw.circle(surface, color, (x, y), R, w)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()