#!usr/bin/env python
#-*- coding: utf-8 -*-

import sys,pygame
from pygame.locals import *
#Constantes
WIDTH = 200
HEIGHT = 200


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Nombre Pygame")

    fuente=pygame.font.Font(None,20)
    text="Erick Bolaños"
    mensaje=fuente.render(text,1,(255,255,255))
    screen.blit(mensaje, (20,20))
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
#if __name__ =="__main__":
    
#   main()
