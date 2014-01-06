# -*- coding: utf-8 -*-
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
###
###
#DON'T IMPORT A MODULE THAT IMPORTS THIS FILE (CONFIG) => CYCLIC IMPORTS
import pygame, pygame.font, codecs, os, img 
##
##
       
            
SIZE = HEIGHT, WIDTH = 1000, 600
START_SIZE = (700,300)
FRAMERATE = 30

IMG_PATH = "images/"
FONT_PATH = "fonts/"

#ICON = os.path.join(IMG_PATH, "icon.ico")
CAPTION = "Kawa - Fluss"

SCREEN = pygame.display.set_mode(START_SIZE, pygame.DOUBLEBUF, 32)
BUFFER = pygame.Surface(SIZE, flags=pygame.SRCALPHA)

FONT = os.path.join(FONT_PATH, "DroidSans.ttf")
FONT_SIZE = 13
FONT_COLOR = (179,1,99)
FONT_SIZE_START = 15
FONT_COLOR_START = (0,0,0)

BOX_PADDING = 4
BOX_COLOR = (0,0,0)
BOX_FOCUS_COLOR = (179,1,99) # Magenta
BOX_EMPTY_COLOR = (255,100,100)
BOX_COLORS = [BOX_COLOR,BOX_FOCUS_COLOR,BOX_EMPTY_COLOR]


PIC_CONTINUE = pygame.image.load(os.path.join(IMG_PATH, "continue.png"))
PIC_POPUP = pygame.image.load(os.path.join(IMG_PATH, "popup.png"))
#PIC_STONE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_PATH, "stone.png")), (100,75)).convert_alpha()
PIC_STONE1 = pygame.image.load(os.path.join(IMG_PATH, "stone1.png"))
PIC_STONE2 = pygame.image.load(os.path.join(IMG_PATH, "stone2.png"))
PIC_STONE3 = pygame.image.load(os.path.join(IMG_PATH, "stone3.png"))
PIC_STONE4 = pygame.image.load(os.path.join(IMG_PATH, "stone4.png"))
PIC_STONE5 = pygame.image.load(os.path.join(IMG_PATH, "stone5.png"))
PIC_STONE6 = pygame.image.load(os.path.join(IMG_PATH, "stone6.png"))
PIC_WOOD1 = pygame.image.load(os.path.join(IMG_PATH, "Wood1.png"))
PIC_WOOD2 = pygame.image.load(os.path.join(IMG_PATH, "Wood2.png"))
PIC_WOOD3 = pygame.image.load(os.path.join(IMG_PATH, "Wood3.png"))
PIC_WOOD4 = pygame.image.load(os.path.join(IMG_PATH, "Wood4.png"))
PIC_WOOD5 = pygame.image.load(os.path.join(IMG_PATH, "Wood5.png"))
PIC_WOOD6 = pygame.image.load(os.path.join(IMG_PATH, "Wood6.png"))
PIC_STONE_BUTTON1_UP = pygame.image.load(os.path.join(IMG_PATH, 'StoneButton1up.png'))
PIC_STONE_BUTTON1_DOWN = pygame.image.load(os.path.join(IMG_PATH, 'StoneButton1down.png'))
PIC_STONE_BUTTON2_UP = pygame.image.load(os.path.join(IMG_PATH, 'StoneButton2up.png'))
PIC_STONE_BUTTON2_DOWN = pygame.image.load(os.path.join(IMG_PATH, 'StoneButton2down.png'))
PIC_STONE_BUTTON3_UP = pygame.image.load(os.path.join(IMG_PATH, 'StoneButton3up.png'))
PIC_STONE_BUTTON3_DOWN = pygame.image.load(os.path.join(IMG_PATH, 'StoneButton3down.png'))
PIC_STONE_BUTTON4_UP = pygame.image.load(os.path.join(IMG_PATH, 'StoneButton4up.png'))
PIC_STONE_BUTTON4_DOWN = pygame.image.load(os.path.join(IMG_PATH, 'StoneButton4down.png'))
PIC_STONE_BUTTON5_UP = pygame.image.load(os.path.join(IMG_PATH, 'StoneButton5up.png'))
PIC_STONE_BUTTON5_DOWN = pygame.image.load(os.path.join(IMG_PATH, 'StoneButton5down.png'))
PIC_STONE_BUTTON6_UP = pygame.image.load(os.path.join(IMG_PATH, 'StoneButton6up.png'))
PIC_STONE_BUTTON6_DOWN = pygame.image.load(os.path.join(IMG_PATH, 'StoneButton6down.png'))
PIC_WOOD_BUTTON1_UP = pygame.image.load(os.path.join(IMG_PATH, 'WoodButton1up.png'))
PIC_WOOD_BUTTON1_DOWN = pygame.image.load(os.path.join(IMG_PATH, 'WoodButton1down.png'))
PIC_WOOD_BUTTON2_UP = pygame.image.load(os.path.join(IMG_PATH, 'WoodButton2up.png'))
PIC_WOOD_BUTTON2_DOWN = pygame.image.load(os.path.join(IMG_PATH, 'WoodButton2down.png'))
PIC_WOOD_BUTTON3_UP = pygame.image.load(os.path.join(IMG_PATH, 'WoodButton3up.png'))
PIC_WOOD_BUTTON3_DOWN = pygame.image.load(os.path.join(IMG_PATH, 'WoodButton3down.png'))
PIC_WOOD_BUTTON4_UP = pygame.image.load(os.path.join(IMG_PATH, 'WoodButton4up.png'))
PIC_WOOD_BUTTON4_DOWN = pygame.image.load(os.path.join(IMG_PATH, 'WoodButton4down.png'))
PIC_WOOD_BUTTON5_UP = pygame.image.load(os.path.join(IMG_PATH, 'WoodButton5up.png'))
PIC_WOOD_BUTTON5_DOWN = pygame.image.load(os.path.join(IMG_PATH, 'WoodButton5down.png'))
PIC_WOOD_BUTTON6_UP = pygame.image.load(os.path.join(IMG_PATH, 'WoodButton6up.png'))
PIC_WOOD_BUTTON6_DOWN = pygame.image.load(os.path.join(IMG_PATH, 'WoodButton6down.png'))
PIC_UNDO_BTN_UP = pygame.image.load(os.path.join(IMG_PATH, 'UndoUp.png'))
PIC_UNDO_BTN_DOWN = pygame.image.load(os.path.join(IMG_PATH, 'UndoDOWN.png'))
PIC_SAVE_BTN_UP = pygame.image.load(os.path.join(IMG_PATH, 'SaveUp.png'))
PIC_SAVE_BTN_DOWN = pygame.image.load(os.path.join(IMG_PATH, 'SaveDown.png'))
PIC_NEW_BTN_UP = pygame.image.load(os.path.join(IMG_PATH, 'NewUp.png'))
PIC_NEW_BTN_DOWN = pygame.image.load(os.path.join(IMG_PATH, 'NewDown.png'))
PIC_TRASH_BTN_UP = pygame.image.load(os.path.join(IMG_PATH, 'CancelUp.png'))
PIC_TRASH_BTN_DOWN = pygame.image.load(os.path.join(IMG_PATH, 'CancelDown.png'))
PIC_OK_BTN_UP = pygame.image.load(os.path.join(IMG_PATH, 'OKButton.png'))
PIC_OK_BTN_DOWN = pygame.image.load(os.path.join(IMG_PATH, 'OKButtonDown.png'))
PIC_CANCEL_BTN_UP = pygame.image.load(os.path.join(IMG_PATH, 'AbbrechenButton.png'))
PIC_CANCEL_BTN_DOWN = pygame.image.load(os.path.join(IMG_PATH, 'AbbrechenButtonDown.png'))
##Riverbed Minis
PIC_RIVERBED_MINI1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_PATH, "riverbed1.png")), (281,200)).convert_alpha()
PIC_RIVERBED_MINI2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_PATH, "riverbed2.png")), (281,200)).convert_alpha()
PIC_RIVERBED_MINI3 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_PATH, "riverbed3.png")), (281,200)).convert_alpha()
PIC_RIVERBED_MINI4 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_PATH, "riverbed4.png")), (281,200)).convert_alpha()
PIC_RIVERBED_MINI5 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_PATH, "riverbed5.png")), (281,200)).convert_alpha()
PIC_RIVERBED_MINI6 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_PATH, "riverbed6.png")), (281,200)).convert_alpha()
            


START_SCREEN_TEXT = codecs.decode("""Michael Iwama ist Professor am Institut für Arbeitswissenschaft und 
Ergotherapie an der Universität in Toronto.
Im Jahre 2006 hat er ein ergotherapeutisches Modell entwickelt,
dem eine ganzheitliche und kulturberücksichtigende Sichtweise zu Grunde liegt.

Der ursprüngliche Gedanke war, die Ergotherapie und deren Wert im 
sozialen asiatischen Kontextzu beschreiben und zu erklären. 
Dem ging eine Frage der japanischen Ergotherapeuten voraus,
nämlich inwieweit sind die Kernideen und Konzepte der Ergotherapie,
welche sich hauptsächlich auf kulturelle Eigenheiten und Normen 
nordamerikanischer soziokultureller Kontexte befasst hat, für andere
Kulturkreise anwendbar?
""", "utf-8" )

POP_UP_ITEM_TEXT =  codecs.decode("Bitte Beschreibung eingeben und bestaetigen", "utf-8")
POP_UP_SAVE_TEXT = codecs.decode("Bitte Dateinamen für das zu speichernde Bild eingeben", "utf-8")


RIVERBED_LIST = [pygame.image.load(IMG_PATH + 'riverbed1.png'),
                 pygame.image.load(IMG_PATH + 'riverbed2.png'),
                 pygame.image.load(IMG_PATH + 'riverbed3.png'),
                 pygame.image.load(IMG_PATH + 'riverbed4.png'),
                 pygame.image.load(IMG_PATH + 'riverbed5.png'),
                 pygame.image.load(IMG_PATH + 'riverbed6.png')]

                 
COLORMAPS = [ pygame.image.load(os.path.join(IMG_PATH, "colormap1.png")),
              pygame.image.load(os.path.join(IMG_PATH, "colormap2.png")),
              pygame.image.load(os.path.join(IMG_PATH, "colormap3.png")),
              pygame.image.load(os.path.join(IMG_PATH, "colormap4.png")),
              pygame.image.load(os.path.join(IMG_PATH, "colormap5.png")),
              pygame.image.load(os.path.join(IMG_PATH, "colormap6.png"))]
              
def makeBorder(surface, color = (255,255,255), width=2):
    pygame.draw.rect(surface, color, (0,0,surface.get_width(),surface.get_height()), width)
    return surface
             
THUMBNAILS = [ makeBorder(pygame.transform.scale(PIC_STONE1.copy(), (32+i*8,24+i*6))) for i in range(0,6)]
                



RIVERBED_SIZE = (690, 490)


CLOCK = pygame.time.Clock()


def CLEAR(surface):
    surface.fill((255, 255, 255, 0))
    return surface

