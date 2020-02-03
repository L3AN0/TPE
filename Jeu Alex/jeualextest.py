# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 10:22:42 2020

@author: ARNIAUD
"""

import pygame
import time
from pygame.locals import *
 
pygame.init()
 
info = pygame.display.Info()
 
fenetre = pygame.display.set_mode((1920,1080), FULLSCREEN)
scrrec = fenetre.get_rect()
 
fond_Original = pygame.image.load("fondtest.png").convert()
fond_Vierge = pygame.image.load("fond.png").convert()
fond_20 = pygame.image.load("arouf20.png").convert()
fond_40 = pygame.image.load("arouf40.png").convert()
fond_60 = pygame.image.load("arouf60.png").convert()
fond_80 = pygame.image.load("arouf80.png").convert()
fond_100 = pygame.image.load("arouf100.png").convert()
fond = fond_Original
liste = [fond_Vierge, fond_20, fond_40, fond_60, fond_80, fond_100]
 
fond = pygame.transform.scale(fond, (scrrec.right, scrrec.bottom))
dimension_fondx = fond.get_width()
dimension_fondy = fond.get_height()
 
position_fond = (0,0)
 
fenetre.blit(fond, position_fond)
 
pygame.display.flip()
son = pygame.mixer.Sound("rasputin.wav")
son.stop()
 
continuer = True
prems = True 

while continuer:
 
    for event in pygame.event.get():
 
        if event.type == QUIT:
            continuer = False
 
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                continuer = False
            if event.key == K_RETURN and prems:
                    son.stop()
                    son = pygame.mixer.Sound("aroufmusic.wav")
                    son.stop()
                    for image in liste:
                        fond = pygame.transform.scale(image, (scrrec.right, scrrec.bottom))
                        fenetre.blit(fond, position_fond)
                        pygame.display.flip()
                        time.sleep(0.8)
                    prems = False
                        
                
                


 
    fenetre.blit(fond, position_fond)
    pygame.display.flip()
 
pygame.quit()