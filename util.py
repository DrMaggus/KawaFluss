import pygame, pygame.font

from InputBox import InputBox
from config import *

def show_start_window(size):
    #change screen size
    screen = pygame.display.set_mode(size, pygame.DOUBLEBUF, 32)
    button_rect = (screen.get_width() - 100, screen.get_height() - 58, PIC_CONTINUE.get_width(), PIC_CONTINUE.get_height())
    #screen background?
    screen.fill((255,255,255))
    height = 0
    top_padding = 30
    
    #for each line in text print to screen
    for line in START_SCREEN_TEXT.split('\n'):
        line_rend = pygame.font.Font( FONT, FONT_SIZE_START).render( line.strip(), True, FONT_COLOR_START )
        screen.blit(line_rend, (screen.get_width()/2- line_rend.get_width()/2, height + top_padding )) #center
        height += 18
        
    screen.blit(PIC_CONTINUE, (screen.get_width() - 100, screen.get_height() - 58) )
    
    running = True
    button_down = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #mouse over button ?
                mouse = pygame.mouse.get_pos()
                if mouse[0] > button_rect[0] and mouse[0] < button_rect[0]+button_rect[2] \
                            and mouse[1] > button_rect[1] and mouse[1] < button_rect[1]+button_rect[3]:
                    button_down = True
            if event.type == pygame.MOUSEBUTTONUP and button_down:
                mouse = pygame.mouse.get_pos()
                if mouse[0] > button_rect[0] and mouse[0] < button_rect[0]+button_rect[2] \
                            and mouse[1] > button_rect[1] and mouse[1] < button_rect[1]+button_rect[3]:
                    running = False
                
        pygame.display.flip() 
        
    #change screen size
    pygame.display.set_mode(SIZE, pygame.DOUBLEBUF, 32)
    

#TODO: return inputtext
def show_popup():
    background = SCREEN.copy()
    input = InputBox((360,280), BUFFER, color=[(179,179,179),(0,186,220),(179,179,179)], max_size=280)
    text = pygame.font.Font( FONT, FONT_SIZE).render( "Bitte Beschreibung eingeben und bestaetigen", True, (0,0,0) )
    running = True
    while running:
        CLEAR(BUFFER)
        SCREEN.blit(background,(0,0))
        SCREEN.blit(PIC_POPUP,(0,0))
        SCREEN.blit(text,(365,245))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
            input.handleEvent(event)
            
        input.update(SCREEN)
        pygame.display.update()
        
        
        
        
        
        