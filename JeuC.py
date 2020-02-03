# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import pygame,random
from constantes import*

from pygame.locals import *
pygame.init()
fenetre = pygame.display.set_mode((1920,1080),FULLSCREEN)
fond = pygame.image.load(bloc).convert()
fenetre.blit(fond,(0,0))
pygame.display.flip()
continuer = True
tous_les_blocks =[]

niveau= []



while continuer:
    for event in pygame.event.get():  
        if event.type == QUIT:
            continuer = False 
        
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                continuer = False

    
    for i in range(len(tous_les_blocks)):
        block = random.choice(tous_les_blocks)
        niveau.append(block)
        tous_les_blocks.remove(block)
    print(niveau)
pygame.quit()