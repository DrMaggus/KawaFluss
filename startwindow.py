###############################################
#
#             KAWA-FLUSS MODELL
#
#
#                Written by
#        Matthias Eiserloh, Markus Wolf
#
#
#          Copyright (c) 2013 by 
#          M. Eiserloh and M. Wolf
#
#
################################################

import pygame, pygame.font
from config import *

def show_start_window(size):
    #change screen size
    screen = pygame.display.set_mode(size, pygame.DOUBLEBUF, 32)
    continue_button = pygame.image.load( PIC_CONTINUE )
    button_rect = (screen.get_width() - 100, screen.get_height() - 58, continue_button.get_width(), continue_button.get_height())
    #screen background?
    screen.fill((255,255,255))
    height = 0
    top_padding = 30
    
    #for each line in text print to screen
    for line in START_SCREEN_TEXT.split('\n'):
        line_rend = pygame.font.Font( FONT, FONT_SIZE_START).render( line.strip(), True, FONT_COLOR_START )
        screen.blit(line_rend, (screen.get_width()/2- line_rend.get_width()/2, height + top_padding )) #center
        height += 18
        
    screen.blit(continue_button, (screen.get_width() - 100, screen.get_height() - 58) )
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #mouse over button ?
                mouse = pygame.mouse.get_pos()
                if mouse[0] > button_rect[0] and mouse[0] < button_rect[0]+button_rect[2] \
                            and mouse[1] > button_rect[1] and mouse[1] < button_rect[1]+button_rect[3]:
                    running = False
        pygame.display.flip() 
        
    #change screen size
    pygame.display.set_mode(SIZE, pygame.DOUBLEBUF, 32)