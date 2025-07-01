import pygame
from sys import exit

# Switching pygame on
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Runner/font/Pixeltype.ttf', 50)

# 'Static' surface
sky_surface = pygame.image.load('Runner/graphics/Sky.png').convert()
ground_surface = pygame.image.load('Runner/graphics/ground.png').convert()
text_surface = test_font.render('RUNNER', False, 'Black')

# 'Dynamic ' Surface
snail_surface = pygame.image.load('Runner/graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600

player_surface = pygame.image.load('Runner/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Block Image Transfer...one image on another        
    screen.blit(sky_surface,(0, 0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface, (350, 50))
    snail_x_pos -= 4
    if snail_x_pos < -100: snail_x_pos = 900
    screen.blit(snail_surface, (snail_x_pos,270))
    screen.blit(player_surface, player_rect)



    #draw all the elements and update everything
    pygame.display.update()
    clock.tick(60)