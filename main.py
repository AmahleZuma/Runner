import pygame
from sys import exit

# Switching pygame on
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

test_surface = pygame.Surface((100,200))
test_surface.fill('Red')

# Test 1.0
new_surface = pygame.Surface((200, 400))
new_surface.fill('Green')

# Test 1.2
overlay_surface = pygame.Surface((200, 200))
overlay_surface.fill('Purple')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Block Image Transfer...one image on another        
    screen.blit(test_surface,(0,0))
    screen.blit(new_surface,(100,50))
    screen.blit(overlay_surface, (100,50))  # missed a comma


    #draw all the elements and update everything
    pygame.display.update()
    clock.tick(60)