import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surface = score_font.render(str(current_time), False, (64, 64, 64))
    score_rect = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rect)

# Switching pygame on
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
score_font = pygame.font.Font('Runner/font/Pixeltype.ttf', 50)
game_active = True
start_time = 0

# 'Static' surface
sky_surface = pygame.image.load('Runner/graphics/Sky.png').convert()
ground_surface = pygame.image.load('Runner/graphics/ground.png').convert()

# Score Surface
# score_surface = score_font.render('RUNNER', False, (64, 64, 64))
# score_rect = score_surface.get_rect(center = (400, 50))

# Restart Surface
restart_surface = score_font.render('PRESS SPACE TO RESTART', False, (250, 250, 250))
restart_rect = restart_surface.get_rect(center = (400, 100))

# 'Dynamic ' Surface
# Snail
snail_surface = pygame.image.load('Runner/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,300))

# Player
player_surface = pygame.image.load('Runner/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                        player_gravity = -25
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                      game_active = True
                      snail_rect.left = 800 
                      start_time = int(pygame.time.get_ticks()/1000)

    if game_active:
        #Block Image Transfer...one image on another        

        # Drawing the sky, floor and title
        screen.blit(sky_surface,(0, 0))
        screen.blit(ground_surface,(0,300))

        # Adding a background pad
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        # screen.blit(score_surface, score_rect)
        display_score()

        # Drawing the snail and using geometric tricks to give it a looping effect
        snail_rect.left -= 4
        if snail_rect.left <= -50: snail_rect.left = 900
        screen.blit(snail_surface, snail_rect)

        # Drawing the player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surface, player_rect)


        # Collision
        if snail_rect.colliderect(player_rect):
            game_active = False

    else:
         screen.fill("Blue")
         screen.blit(restart_surface, restart_rect)



    #draw all the elements and update everything
    pygame.display.update()
    clock.tick(60)









































# The Shadow Realm of Forsaken Code:
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print('jump')


    # Checking if a collison has indeed occured 
    # Specifically if the rectangles are overlapping...this method is a massive issue for health bar related functions
    # if player_rect.colliderect(snail_rect):
    #     print("Collision")

    # This determines whether or not the mouse pointer has collided with the player and what buttons were pressed exactly
    # mouse_pos = pygame.mouse.get_pos()
    # if  player_rect.collidepoint((mouse_pos)):
    #     print(True)

    # Drawing circles for vibes
    # pygame.draw.ellipse(screen, 'Red', player_rect)
    # pygame.draw.ellipse(screen, 'Red', snail_rect)