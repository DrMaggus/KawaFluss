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

import pygame, pygame.font, codecs, os, button, img

SIZE = HEIGHT, WIDTH = 1000, 600
START_SIZE = (700,300)
FRAMERATE = 30

IMG_PATH = "images/"
FONT_PATH = "fonts/"

#ICON = os.path.join(IMG_PATH, "icon.ico")
CAPTION = "Kawa - Fluss"

SCREEN = pygame.display.set_mode(START_SIZE, pygame.DOUBLEBUF, 32)

FONT = os.path.join(FONT_PATH, "DroidSans.ttf")
FONT_SIZE = 13
FONT_COLOR = (179,1,99)
FONT_SIZE_START = 15
FONT_COLOR_START = (0,0,0)

BOX_PADDING = 4
BOX_COLOR = None
BOX_FOCUS_COLOR = (179,1,99) # Magenta
BOX_EMPTY_COLOR = (255,100,100)

STONE_COLOR = (51,51,51)

PIC_CONTINUE = os.path.join(IMG_PATH, "continue.png")

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

RIVER_BTN_POS1 = 50, 100
RIVER_BTN_POS2 = 367, 100
RIVER_BTN_POS3 = 684, 100
RIVER_BTN_POS4 = 50, 350
RIVER_BTN_POS5 = 367, 350
RIVER_BTN_POS6 = 684, 350

RIVERBED_LIST = [pygame.image.load(IMG_PATH + 'riverbed1.png'),\
                 pygame.image.load(IMG_PATH + 'riverbed1.png'),\
                 pygame.image.load(IMG_PATH + 'riverbed1.png'),\
                 pygame.image.load(IMG_PATH + 'riverbed2.png'),\
                 pygame.image.load(IMG_PATH + 'riverbed2.png'),\
                 pygame.image.load(IMG_PATH + 'riverbed2.png')]
                
STONE = pygame.image.load(IMG_PATH + 'stone.png')
STONE_BUTTON_UP = pygame.image.load(IMG_PATH + 'stone_button_up.png')
STONE_BUTTON_DOWN = pygame.image.load(IMG_PATH + 'stone_button_down.png')

WOOD_STONE_BTN_LIST = button.WoodnStoneBtns([((800, 20), STONE_BUTTON_UP, STONE_BUTTON_DOWN, img.Img(0, 0, False, False, 0, STONE, STONE)),\
                                             ((800, 170), STONE_BUTTON_UP, STONE_BUTTON_DOWN, img.Img(0, 0, False, False, 0, STONE, STONE)),\
                                             ((800, 320), STONE_BUTTON_UP, STONE_BUTTON_DOWN, img.Img(0, 0, False, False, 0, STONE, STONE))])
    

CLOCK = pygame.time.Clock()

    