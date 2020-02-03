# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 11:17:59 2020

@author: isnard
"""
fichier = open("map.py","w")
fichier.write("map={[,,,,,,,,,,,,,,,]\n")
for i in range(8):
    fichier.write("[,,,,,,,,,,,,,,,]\n")
    
fichier.close()