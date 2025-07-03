import pygame
from sys import exit

# Switching pygame on
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
score_font = pygame.font.Font('Runner/font/Pixeltype.ttf', 50)

# 'Static' surface
sky_surface = pygame.image.load('Runner/graphics/Sky.png').convert()
ground_surface = pygame.image.load('Runner/graphics/ground.png').convert()
score_surface = score_font.render('RUNNER', False, 'Black')
score_rect = score_surface.get_rect(center = (400, 50))


# 'Dynamic ' Surface

# Snail
snail_surface = pygame.image.load('Runner/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,300))

# Player
player_surface = pygame.image.load('Runner/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type ==  pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print('Collision!')
                 

            
        

    #Block Image Transfer...one image on another        

    # Drawing the sky, floor and title
    screen.blit(sky_surface,(0, 0))
    screen.blit(ground_surface,(0,300))

    # Adding a background pad
    pygame.draw.rect(screen, 'Pink', score_rect)
    pygame.draw.rect(screen, 'Pink', score_rect, 10)

    screen.blit(score_surface, score_rect)

    # Drawing the snail and using geometric tricks to give it a looping effect
    snail_rect.left -= 4
    if snail_rect.left <= -50: snail_rect.left = 900
    screen.blit(snail_surface, snail_rect)

    # Drawing the player
    screen.blit(player_surface, player_rect)


    # Checking if a collison has indeed occured 
    # Specifically if the rectangles are overlapping...this method is a massive issue for health bar related functions
    # if player_rect.colliderect(snail_rect):
    #     print("Collision")

    # This determines whether or not the mouse pointer has collided with the player and what buttons were pressed exactly
    # mouse_pos = pygame.mouse.get_pos()
    # if  player_rect.collidepoint((mouse_pos)):
    #     print(True)

    pygame.draw.ellipse(screen, 'Red', player_rect)



    #draw all the elements and update everything
    pygame.display.update()
    clock.tick(60)