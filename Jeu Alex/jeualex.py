# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import pygame
from pygame.locals import *
pygame.init()
fenetre = pygame.display.set_mode((1920,1080))
fond = pygame.image.load("fond.png").convert()
fenetre.blit(fond, (0,0))
pygame.display.flip()

continuer = True

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
            pygame.quit()