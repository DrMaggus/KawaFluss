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
START_SIZE = (730,635)
RIVERBED_SIZE = (690, 490)
RIVERBED_POS = (20,88)
FRAMERATE = 30

IMG_PATH = "images/"
FONT_PATH = "fonts/"

ICON = os.path.join(IMG_PATH, "icon.jpg")
CAPTION = "Kawa - Fluss"

SCREEN = pygame.display.set_mode(START_SIZE, pygame.DOUBLEBUF, 32)
BUFFER = pygame.Surface(SIZE, flags=pygame.SRCALPHA)

FONT = os.path.join(FONT_PATH, "CosmicSansNeueMono.ttf")
FONT_SIZE = 13
FONT_COLOR = (49,200,49)
FONT_SIZE_START = 15
FONT_COLOR_START = (0,0,0)
FONT_COLOR_POPUP = (0,0,0)

BOX_PADDING = 4
BOX_COLOR = None
BOX_FOCUS_COLOR = (179,1,99) # Magenta
BOX_EMPTY_COLOR = (8,138,8)
BOX_COLORS = [BOX_COLOR,BOX_FOCUS_COLOR,BOX_EMPTY_COLOR]

TEXT_ON_IMG_COLOR = (255,0,41)

PIC_CONTINUE = pygame.image.load(os.path.join(IMG_PATH, "continue.png"))
PIC_CONTINUE_HOVER = pygame.image.load(os.path.join(IMG_PATH, "continue2.png"))
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
PIC_UNDO_BTN_DOWN = pygame.image.load(os.path.join(IMG_PATH, 'UndoDown.png'))
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
PIC_CREDITS = pygame.image.load(os.path.join(IMG_PATH, 'credits.png'))
##Riverbed Minis
PIC_RIVERBED_MINI1 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_PATH, "riverbed1.png")), (281,200)).convert_alpha()
PIC_RIVERBED_MINI2 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_PATH, "riverbed2.png")), (281,200)).convert_alpha()
PIC_RIVERBED_MINI3 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_PATH, "riverbed3.png")), (281,200)).convert_alpha()
PIC_RIVERBED_MINI4 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_PATH, "riverbed4.png")), (281,200)).convert_alpha()
PIC_RIVERBED_MINI5 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_PATH, "riverbed5.png")), (281,200)).convert_alpha()
PIC_RIVERBED_MINI6 = pygame.transform.scale(pygame.image.load(os.path.join(IMG_PATH, "riverbed6.png")), (281,200)).convert_alpha()
            
BOLD_WORDS = [codecs.decode(word,"utf-8") for word in ["der Fluss", "Wasser","Flussbett","Steine", "Treibholz", "Sinn und Zweck"]]

START_SCREEN_TEXT = codecs.decode("""
Das KAWA-Modell ist eine Theorie über Betätigung und Ergotherapie, die in Asien
entwickelt wurde. Zur Darstellung des fernöstlichen Bildes von Selbst und Kontext
dient eine Naturmetapher:          . Dieser soll die momentane Lebenssituation
eines Individuums darstellen.
 
Das        (jap. Mizu) repräsentiert die Lebensenergie/den Lebensfluss des 
Menschen. Die Qualität des Fließens wird vor allem beeinflusst durch
das           (jap. Torimaki), das die soziale und physikalische Umwelt einer Person
repräsentiert.        (jap. Iwa), die in Größe und Anzahl variieren können, 
verkörpern die Probleme und Herausforderungen des täglichen Lebens. In 
Kombination mit dem Flussbett (Umweltfaktoren) können Lebensfluss,
Wohlergehen und Betätigung ermöglicht oder verhindert 
werden.           (jap. Ryuboku), das Ressourcen und Barrieren darstellen soll 
(z.B.: materielle/immaterielle Werte, Charakter, Fertigkeiten, Neigungen), 
kann gegen feste Strukturen (Steine und Wände) stoßen oder sich daran reiben und 
so ein größeres Flussbett schaffen, es kann aber auch von denselben Strukturen 
abgefangen werden und so größere Hindernisse im Fluss bilden. Die Räume 
zwischen den Hindernissen (jap. Sukima), durch die die Lebensenergie des 
Klienten fließen kann, repräsentieren „Betätigung“ in einer ostasiatischen 
Perspektive und sind somit Hauptanliegen der Ergotherapie.

Der                 der Ergotherapie in dieser metaphorischen Repräsentation des 
Menschen besteht darin, den Lebensfluss unserer Klienten zu ermöglichen und zu 
verstärken. Um das Leben wieder fließen zu lassen, erfasst der/die Therapeut/in 
die Komplexität der Betätigung im Kontext und sucht nach möglichen Wegen, um
Partizipation zu ermöglichen.



Mit diesem auf dem KAWA-Modell basierenden Programm können nun auch motorisch 
stark eingeschränkte Klienten ihren Fluss „malen“.
""", "utf-8" )

START_SCREEN_SOURCE = codecs.decode(
"""Kubny-Lüke, B. (2003). Ergotherapie im Arbeitsfeld Psychiatrie. 2. Überarb. Aufl. Stuttgart: Georg Thieme Verlag.
S.95-99.""", "utf-8" )

POP_UP_ITEM_TEXT =  codecs.decode("Bitte Beschreibung eingeben und bestaetigen", "utf-8")
POP_UP_SAVE_TEXT = codecs.decode("Bitte Dateinamen für das zu speichernde Bild eingeben", "utf-8")

CREDITS_HEADER =  [codecs.decode(word,"utf-8") for word in ["PROGRAMMING","DESIGN","SPECIAL THANKS"]]
CREDITS_NAMES =  [codecs.decode(word,"utf-8") for word in ["Matthias Eiserloh", "Markus Wolf","Vincent Grahn", "to all testers for their effort and input","to Vincent for his amazing artwork"]]



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
                              


CLOCK = pygame.time.Clock()

FORBIDDEN_KEYS = [pygame.K_TAB,pygame.K_UP,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_LEFT,pygame.K_INSERT,pygame.K_HOME,
                  pygame.K_END, pygame.K_PAGEUP, pygame.K_PAGEDOWN, pygame.K_F1, pygame.K_F2, pygame.K_F3,   
                  pygame.K_F4,pygame.K_F5,pygame.K_F6,pygame.K_F7, pygame.K_F8,pygame.K_F9, pygame.K_F10 ,   
                  pygame.K_F11,pygame.K_F12,pygame.K_F13,pygame.K_NUMLOCK, pygame.K_CAPSLOCK,pygame.K_SCROLLOCK ,pygame.K_RSHIFT, pygame.K_LSHIFT ,   
                  pygame.K_RCTRL, pygame.K_LCTRL, pygame.K_RALT,pygame.K_LALT , pygame.K_RMETA  ,pygame.K_LMETA]


def CLEAR(surface):
    surface.fill((255, 255, 255, 0))
    return surface

