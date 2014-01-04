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
PIC_STONE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_PATH, "stone.png")), (100,75)).convert_alpha()
PIC_STONE_BUTTON_UP = pygame.image.load(os.path.join(IMG_PATH, 'stone_button_up.png'))
PIC_STONE_BUTTON_DOWN = pygame.image.load(os.path.join(IMG_PATH, 'stone_button_down.png'))
PIC_ARROW_UNDO_UP = pygame.image.load(os.path.join(IMG_PATH, 'arrowUndo.png'))
PIC_SAVE_BTN_UP = pygame.image.load(os.path.join(IMG_PATH, 'saveBtn.png'))
PIC_MENU = pygame.image.load(os.path.join(IMG_PATH, 'menu.png'))

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
                



RIVERBED_SIZE = (690, 490)


CLOCK = pygame.time.Clock()

STONE_BTN_1 = 0
STONE_BTN_2 = 1
STONE_BTN_3 = 2
STONE_BTN_4 = 3
STONE_BTN_5 = 4
STONE_BTN_6 = 5
WOOD_BTN_1 = 6
WOOD_BTN_2 = 7
WOOD_BTN_3 = 8
WOOD_BTN_4 = 9
WOOD_BTN_5 = 10
WOOD_BTN_6 = 11

def CLEAR(surface):
    surface.fill((255, 255, 255, 0))
