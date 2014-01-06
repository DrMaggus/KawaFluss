# -*- coding: utf-8 -*-
import pygame, pygame.font, time, sys, button

from inputbox import InputBox
from config import *

##IN CONFIG
riverbedMini1 = pygame.image.load(IMG_PATH + 'riverbed1mini.png')
riverbedMini2 = pygame.image.load(IMG_PATH + 'riverbed2mini.png')
LEFT = 1

class Log():
    def __init__(self, msg, status = "debug"):
        #TODO delete file when to big
        msg_type = {"debug":msg+"\n","warn":"## Warning ##  "+msg+"\n","err":"## Error ##  "+msg+"\n"}[status]
        #create file if not existent
        file = open("kawafluss.log","a")
        file.write("%s - %s" % (time.strftime("%c"),msg_type))
        file.close()
        import sys
        sys.stdout.write(">>  " + msg_type)

def show_start_window(size):
    Log("Display infomation window")
    #change screen size
    screen = pygame.display.set_mode(size, pygame.DOUBLEBUF, 32)
    Log("Change screen size to "+str(size))
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
    Log("Change screen size to "+str(SIZE))
    

        #TODO POPUP OK-Button
def show_popup(task, textPosition):
    Log("Open Pop up input screen")
    background = SCREEN.copy()
    input = InputBox((360,280), BUFFER, color=[(179,179,179),(0,186,220),(179,179,179)], max_size=280)
    text = pygame.font.Font( FONT, FONT_SIZE ).render(task , True, (0,0,0) )
    running = True
    while running:
        mouseX, mouseY = pygame.mouse.get_pos()
        CLEAR(BUFFER)
        SCREEN.blit(background,(0,0))
        SCREEN.blit(PIC_POPUP,(0,0))
        SCREEN.blit(text,textPosition)
        SCREEN.blit(PIC_OK_BTN_UP, (456, 310))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if show_security():
                    exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
            #Left mouseclick on OK button
            if event.type == pygame.MOUSEBUTTONDOWN and mouse_in_area(mouseX, mouseY, 456, 310, 87, 28) and  event.button == 1: 
                SCREEN.blit(PIC_OK_BTN_DOWN, (456, 310)) 
            if event.type == pygame.MOUSEBUTTONUP and mouse_in_area(mouseX, mouseY, 456, 310, 87, 28) and  event.button == 1:
                running = False
            input.handleEvent(event)
            
        input.update(SCREEN)
        pygame.display.update()
    return input.getString()

        #TODO POPUP OK-Button        
def show_warning(line1, line2, textPos1, textPos2):
    Log("Open Pop up input screen")
    background = SCREEN.copy()
    _line1 = pygame.font.Font( FONT, FONT_SIZE ).render(line1 , True, (0,0,0) )
    _line2 = pygame.font.Font( FONT, FONT_SIZE ).render(line2 , True, (0,0,0) )
    running = True
    while running:
        mouseX, mouseY = pygame.mouse.get_pos()
        CLEAR(BUFFER)
        SCREEN.blit(background,(0,0))
        SCREEN.blit(PIC_POPUP,(0,0))
        SCREEN.blit(_line1, textPos1)
        SCREEN.blit(_line2, textPos2)
        SCREEN.blit(PIC_OK_BTN_UP, (456, 300))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if show_security():
                    exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
            #Left mouseclick on OK button
            if event.type == pygame.MOUSEBUTTONDOWN and mouse_in_area(mouseX, mouseY, 456, 300, 87, 28) and  event.button == 1: 
                SCREEN.blit(PIC_OK_BTN_DOWN, (456, 300)) 
            if event.type == pygame.MOUSEBUTTONUP and mouse_in_area(mouseX, mouseY, 456, 300, 87, 28) and  event.button == 1:
                running = False
        pygame.display.update()

def show_security():
    Log("Open security query screen")
    background = SCREEN.copy()
    text = pygame.font.Font( FONT, FONT_SIZE ).render("Sie sind dabei Ihr Programm zu beenden oder neuzustarten." , True, (0,0,0) )
    answer = True
    running = True
    while running:
        mouseX, mouseY = pygame.mouse.get_pos()
        CLEAR(BUFFER)
        SCREEN.blit(background,(0,0))
        SCREEN.blit(PIC_POPUP,(0,0))
        SCREEN.blit(text, (315,260))
        SCREEN.blit(PIC_OK_BTN_UP, (393, 300))
        SCREEN.blit(PIC_CANCEL_BTN_UP, (520, 300))       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
            #Left mouseclick on OK button
            if event.type == pygame.MOUSEBUTTONDOWN and mouse_in_area(mouseX, mouseY, 393, 300, 87, 28) and  event.button == 1: 
                SCREEN.blit(PIC_OK_BTN_DOWN, (393, 300)) 
            if event.type == pygame.MOUSEBUTTONUP and mouse_in_area(mouseX, mouseY, 393, 300, 87, 28) and  event.button == 1:
                answer = True
                running = False
            #Left mouseclick on CANCEL button
            if event.type == pygame.MOUSEBUTTONDOWN and mouse_in_area(mouseX, mouseY, 520, 300, 87, 28) and  event.button == 1: 
                SCREEN.blit(PIC_CANCEL_BTN_DOWN, (520, 300)) 
            if event.type == pygame.MOUSEBUTTONUP and mouse_in_area(mouseX, mouseY, 520, 300, 87, 28) and  event.button == 1:
                answer = False
                running = False            
        pygame.display.update()
    return answer


def mouse_in_area(mouseX, mouseY, X, Y, width, height):
    if mouseX > X and mouseX < X + width and mouseY > Y and mouseY < Y + height:
        return True
    return False
    
##1.TODO: Funktion um aus Riverbed "Thumbnails" bzw. Minibilder zu machen

##nach 1.TODO =>  'show_riverbed_selection()' in util.py verschieben!
def show_riverbed_selection():
    HEADER = pygame.font.Font( FONT, 45).render( "W�hlen Sie ein Flussbett aus", True, (0,0,0))    
    SCREEN.fill((231, 232, 200))    
    riverbedButton1 = button.Button((50, 100), False, PIC_RIVERBED_MINI1, PIC_RIVERBED_MINI1, None, None)
    riverbedButton2 = button.Button((367, 100), False, PIC_RIVERBED_MINI2, PIC_RIVERBED_MINI2, None, None)
    riverbedButton3 = button.Button((684, 100), False, PIC_RIVERBED_MINI3, PIC_RIVERBED_MINI3, None, None)
    riverbedButton4 = button.Button((50, 350), False, PIC_RIVERBED_MINI4, PIC_RIVERBED_MINI4, None, None)
    riverbedButton5 = button.Button((367, 350), False, PIC_RIVERBED_MINI5, PIC_RIVERBED_MINI5, None, None)
    riverbedButton6 = button.Button((684, 350), False, PIC_RIVERBED_MINI6, PIC_RIVERBED_MINI6, None, None)
   
    riverbedButtonList = [riverbedButton1, riverbedButton2, riverbedButton3, riverbedButton4, riverbedButton5, riverbedButton6]

    running = True
    while running:
        #get mouse position
        mouseX, mouseY = pygame.mouse.get_pos()
        SCREEN.blit(HEADER, (190, 15))
        for btn in riverbedButtonList:
            SCREEN.blit(btn.getImgUnpressed(), (btn.getXY()))
    
        for event in pygame.event.get():
            # Spiel beenden, wenn wir ein QUIT-Event finden.
            if event.type == pygame.QUIT:
                if show_security():
                    sys.exit()
                
            for btn in riverbedButtonList:                                                  
                if event.type == pygame.MOUSEBUTTONUP and btn.mouseOnButton(mouseX, mouseY) and event.button == LEFT:
                    #SCREEN.blit(btn.getImgPressed(), (btn.getXY()))
                    return riverbedButtonList.index(btn)
                            
        # Inhalt von screen anzeigen.
        pygame.display.flip()
        
    
def makeButtonImage(surface):
    unpressed = surface.copy()
    pressed = surface.copy()
    pygame.draw.rect(unpressed, (255,255,255), (0,0,4,surface.get_height()))
    pygame.draw.rect(unpressed, (255,255,255), (0,0,surface.get_width(),3))
    pygame.draw.rect(unpressed, (0,0,0), (0,surface.get_height()-3,surface.get_width(),3))
    pygame.draw.rect(unpressed, (0,0,0), (surface.get_width()-4,0,4,surface.get_height()))
    
    pygame.draw.rect(pressed, (0,0,0), (0,0,4,surface.get_height()))
    pygame.draw.rect(pressed, (0,0,0), (0,0,surface.get_width(),3))
    pygame.draw.rect(pressed, (255,255,255), (0,surface.get_height()-3,surface.get_width(),3))
    pygame.draw.rect(pressed, (255,255,255), (surface.get_width()-4,0,4,surface.get_height()))
    
    return (unpressed, pressed)
        
        
        