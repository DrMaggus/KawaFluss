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
    

#TODO: return inputtext
def show_popup():
    Log("Open Pop up input screen")
    background = SCREEN.copy()
    input = InputBox((360,280), BUFFER, color=[(179,179,179),(0,186,220),(179,179,179)], max_size=280)
    text = pygame.font.Font( FONT, FONT_SIZE ).render( "Bitte Beschreibung eingeben und bestaetigen", True, (0,0,0) )
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
    return input.getString()
        


##1.TODO: Funktion um aus Riverbed "Thumbnails" bzw. Minibilder zu machen

##nach 1.TODO =>  'show_riverbed_selection()' in util.py verschieben!
def show_riverbed_selection():
        
    SCREEN.fill((177, 177, 177))    
    riverbedButton1 = button.Button((50, 100), False, riverbedMini1, riverbedMini1, None, None)
    riverbedButton2 = button.Button((367, 100), False, riverbedMini1, riverbedMini1, None, None)
    riverbedButton3 = button.Button((684, 100), False, riverbedMini1, riverbedMini1, None, None)
    riverbedButton4 = button.Button((50, 350), False, riverbedMini2, riverbedMini2, None, None)
    riverbedButton5 = button.Button((367, 350), False, riverbedMini2, riverbedMini2, None, None)
    riverbedButton6 = button.Button((684, 350), False, riverbedMini2, riverbedMini2, None, None)
   
    riverbedButtonList = [riverbedButton1, riverbedButton2, riverbedButton3, riverbedButton4, riverbedButton5, riverbedButton6]

    running = True
    while running:
        #get mouse position
        mouseX, mouseY = pygame.mouse.get_pos()
        
        for btn in riverbedButtonList:
            SCREEN.blit(btn.getImgUnpressed(), (btn.getXY()))
    
        for event in pygame.event.get():
            # Spiel beenden, wenn wir ein QUIT-Event finden.
            if event.type == pygame.QUIT:
                sys.exit()
                
            for btn in riverbedButtonList:                                                  
                if event.type == pygame.MOUSEBUTTONUP and btn.mouseOnButton(mouseX, mouseY) and event.button == LEFT:
                    #SCREEN.blit(btn.getImgPressed(), (btn.getXY()))
                    return riverbedButtonList.index(btn)
                            
        # Inhalt von screen anzeigen.
        pygame.display.flip()
        
    
def makeButtonImages(surface):
    pass#pygame.draw.rect()
        
        
        
        