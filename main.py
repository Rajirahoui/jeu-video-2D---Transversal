from math import ceil
import pygame
pygame.init()

# Configuration de la fenêtre
pygame.display.set_caption("spy barbie")
screen = pygame.display.set_mode((1080, 720))

# Chargement de l'arrière-plan
background = pygame.image.load("assets/background.jpeg")
background = pygame.transform.scale(background, (1080, 720))

# chargement de la banniere 
banner = pygame.transform.scale(pygame.image.load('assets/banner.png'), (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = ceil(screen.get_width() / 4)

# chargement du bouton play du jeu 
play_button = pygame.transform.scale(pygame.image.load('assets/ticket play.jpeg'), (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = ceil(screen.get_width() / 3.33)
play_button_rect.y = ceil(screen.get_height() / 2)


game_is_running = True
while game_is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False

    # Affichage de l'arrière-plan
    screen.blit(background, (0, 0))  # Change à (0, -200) si voulu
    # affichage la banniere 
    screen.blit(banner, banner_rect)
    # affichage du bouton play 
    screen.blit(play_button, play_button_rect)

    pygame.display.flip()

pygame.quit()
