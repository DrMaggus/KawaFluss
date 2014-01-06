# -*- coding: UTF-8 -*-

import pygame
import placement
import globals
import re

from util import *
from config import *

LEFT = 1
RIGHT = 3

class Button:
    def __init__(self, posXY, is_pressed, img_unpressed, img_pressed, unpressable, mouse_image = None, is_img_on_mouse = None):
            self.posXY = posXY
            self.width = img_pressed.get_width()
            self.height = img_pressed.get_height()
            self.is_pressed = is_pressed
            self.img_pressed = img_pressed
            self.img_unpressed = img_unpressed
            self.unpressable = unpressable
            self.mouse_image = mouse_image
            self.is_img_on_mouse = is_img_on_mouse
            

        
    def getX(self):
        return self.posXY[0]

    def getY(self):
        return self.posXY[1]
    
    def getXY(self):
        return self.posXY

    def setXY(self, _posXY):
        self.posXY = _posXY

    def getWidth(self):
        return self.width

    def setWidth(self, _width):
        self.width = _width

    def getHeight(self):
        return self.height

    def setHeight(self, _height):
        self.height = _height
        
    def getIsPressed(self):
        return self.is_pressed

    def setIsPressed(self, _is_pressed):
        self.is_pressed = _is_pressed
            
    def getImgPressed(self):
        return self.img_pressed
    
    def setImgPressed(self, _img_pressed):
        self.img_pressed = _img_pressed

    def getImgUnpressed(self):
        return self.img_unpressed
    
    def setImgUnpressed(self, _img_unpressed):
        self.img_unpressed = _img_unpressed
        
    def getUnpressable(self):
        return self.unpressable
    
    def setUnpressable(self, _unpressable):
        self.unpressable = _unpressable
            
    def getMouseImage(self):
        return self.mouse_image
    
    def setMouseImage(self, _mouse_image):
        self.mouse_image = _mouse_image
        
    def getIsImgOnMouse(self):
        return self.is_img_on_mouse
    
    def setIsImgOnMouse(self, _is_img_on_mouse):
        self.is_img_on_mouse = _is_img_on_mouse

    def mouseOnButton(self, mouseX, mouseY):
        if mouseX > self.getX() and mouseX < self.getX() + self.getWidth() \
        and mouseY > self.getY() and mouseY < self.getY() + self.getHeight():
            return True
        else:
            return False
        
####### Handles Redo-/Undo-/New- and Save Buttons ######        
class FileBtns:
    def __init__(self, infoList):
        self.buttonList = []
        for item in infoList:
            self.buttonList.append(Button(item[0], False, item[1], item[2], False))
    
    def blitter(self, screen, mouseX, mouseY):
        for btn in self.buttonList:
            #buttons
            if btn.getIsPressed():
                screen.blit(btn.getImgPressed(), (btn.getX(), btn.getY()))
            else:
                screen.blit(btn.getImgUnpressed(), (btn.getX(), btn.getY()))

    def eventHandler(self, event, mouseX, mouseY, placechecker, WoodnStoneBtnList, RiverbedSize, screen):
        if event.type == pygame.MOUSEBUTTONDOWN and self.buttonList[0].mouseOnButton(mouseX, mouseY) and event.button == LEFT:
            self.buttonList[0].setIsPressed(True)
            for btn in WoodnStoneBtnList.getButtonList():
                btn.setIsImgOnMouse(False)
                btn.setUnpressable(False)
                     
        if event.type == pygame.MOUSEBUTTONDOWN and self.buttonList[1].mouseOnButton(mouseX, mouseY) and event.button == LEFT:
            self.buttonList[1].setIsPressed(True)
            if len(WoodnStoneBtnList.getBufferArray())-1 > 0:
                WoodnStoneBtnList.setBufferArray(WoodnStoneBtnList.getBufferArray()[:-1])
                WoodnStoneBtnList.setBuffer()
                placechecker.undo()
                
        
        #SAVE-BUTTON:
        if event.type == pygame.MOUSEBUTTONDOWN and self.buttonList[2].mouseOnButton(mouseX, mouseY) and event.button == LEFT:
            self.buttonList[2].setIsPressed(True) 
            imageToSave = pygame.Surface(RiverbedSize, pygame.SRCALPHA, 32)
            #CLEAR(imageToSave)
            imageToSave.blit(SCREEN, dest=(0,0), area=(20,85,690,490))
            name = show_popup(POP_UP_SAVE_TEXT, (345, 245))
            #Regex matches only alphanumerical letters(no symbols except of "_")
            if not os.path.isdir("save"):
                os.mkdir("save")
            if(re.match(r'\w+\..*', name)):
                if(re.match(r'\w+\.bmp|\w+\.jpg|\w+\.png', name)):
                        pygame.image.save(imageToSave, "save/" + name)
                        show_warning("Speichern war erfolgreich.", \
                                     "", (420, 275), (0,0))     
                        
                    #Does the file already exist? 
                elif os.path.isfile(name):
                    show_warning("Der Dateiname existiert bereits.", \
                                 "", (400, 275), (0,0)) 
                    Log("Save warning:name already exists") 
                else:
                    show_warning("Bitte benutzen sie nur die Dateiendung \".bmp\", \".jpg\" und \".png\".",\
                                 "Alle anderen(auch keine) werden durch .png ersetzt",\
                                 (315, 260), (345, 275))
                    Log("Save warning:wrong ending")
                    name = re.sub(r'\..*', '', name)
                    pygame.image.save(imageToSave, "save/" + name + ".png")
                    show_warning("Speichern als .png-Datei war erfolgreich.", \
                                 "", (380, 275), (0,0))
            elif (re.match(r'.*\W.*', name)):         
                #error handling     
                show_warning("Der Dateiname muss aus mindestens einem Zeichen bestehen", \
                             "und darf nur Buchstaben, Nummern und Unterstriche enthalten.",\
                              (320, 260), (315, 275))
                Log("Save warning:wrong Char")
            #Does the file already exist?            
            elif os.path.isfile(name + ".png"):
                show_warning("Der Dateiname existiert bereits.", \
                             "", (400, 275), (0,0))  
                Log("Save warning:name already exists")
            else:
                pygame.image.save(imageToSave, "save/" + name + ".png")
                show_warning("Speichern war erfolgreich.", \
                             "", (420, 275), (0,0))  
            
        #RESET-BUTTON
        if event.type == pygame.MOUSEBUTTONDOWN and self.buttonList[3].mouseOnButton(mouseX, mouseY) and event.button == LEFT:
            #open river bed selection
            self.buttonList[3].setIsPressed(True) 
            if show_security():
                globals.riverbedNumber = show_riverbed_selection()
                globals.placement = placement.Placement(COLORMAPS[globals.riverbedNumber], (20,85))
                WoodnStoneBtnList.setBufferArray(WoodnStoneBtnList.getBufferArray()[:1])
                WoodnStoneBtnList.setBuffer()
                placechecker.deleteItems()
            
        for btn in self.buttonList:    
            if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                btn.setIsPressed(False)
    
    

####### Handles the Wood and Stone Buttons ######

class WoodnStoneBtns:
    #prepare buffer/bufferArray and create buttons
    #TODO vielleicht argumente anstatt infoList + defaults (siehe InputBox)
    def __init__(self, infoList):
        self.buttonList = []
        self.buffer = pygame.Surface((1000, 600), flags=pygame.SRCALPHA)
        self.buffer.fill((0,0,0,0))
        self.bufferArray = [self.buffer.copy()]
        for item in infoList:
            self.buttonList.append(Button(item[0], False, item[1],  item[2], False,  item[3], False))
    
    def getButton(self, index):
        return self.buttonList[index]
    
    def getButtonList(self):
        return self.buttonList
            
    def getBufferArray(self):
        return self.bufferArray
    
    def isButtonClicked(self):
        for btn in self.buttonList:
            if btn.getIsImgOnMouse():
                return True
        return False
    
    def setBufferArray(self, newArray):
        self.bufferArray = newArray;
    
    def setBuffer(self):
        if len(self.bufferArray)-1 == 0:
            self.buffer.fill((0,0,0,0))
        else:
            self.buffer = self.bufferArray[len(self.bufferArray)-1]

    
    #handles the events
        #- Blit Image to buffer
        #- Image to Mouse
        #- rotation
    def eventHandler(self, event, mouseX, mouseY, placechecker):
        for btn in self.buttonList:
            #Blit Image to Buffer
            if event.type == pygame.MOUSEBUTTONDOWN and btn.getIsImgOnMouse() and event.button == LEFT:
                if placechecker.itemFitOnScreen(btn.getMouseImage().getRotObject()):
                    self.buffer.blit(btn.getMouseImage().getRotObject(),\
                    (mouseX - btn.getMouseImage().getRotObject().get_width()/2, \
                    mouseY - btn.getMouseImage().getRotObject().get_height()/2))
                    self.bufferArray.append(self.buffer.copy())
                    btn.setIsImgOnMouse(False)
                    for button in self.buttonList:
                        button.setUnpressable(False)            
            #Image to Mouse
            if event.type == pygame.MOUSEBUTTONDOWN and btn.mouseOnButton(mouseX, mouseY) and btn.getUnpressable() == False and event.button == LEFT:
                btn.setIsPressed(True)

            if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                btn.setIsPressed(False)
                if btn.mouseOnButton(mouseX, mouseY) and btn.getUnpressable() == False:
                    #TODO: show popup, return and blit input
                    show_popup(POP_UP_ITEM_TEXT, (365,245))
                    btn.getMouseImage().setRotAngle(0)
                    btn.getMouseImage().setRotObject(btn.getMouseImage().getOriginalObject())
                    btn.setIsImgOnMouse(True)
                    for button in self.buttonList:
                        button.setUnpressable(True)
            
            #rotation  
            if event.type == pygame.MOUSEBUTTONDOWN and btn.getIsImgOnMouse() and event.button == RIGHT:
                btn.getMouseImage().setIsRotating(True)
            if event.type == pygame.MOUSEBUTTONUP and btn.getIsImgOnMouse() and event.button == RIGHT:
                btn.getMouseImage().setIsRotating(False)

    #blits the buffer, buttons and MouseImage on the screen            
    def blitter(self, screen, mouseX, mouseY):
        #buffer
        screen.blit(self.bufferArray[len(self.bufferArray)-1], (0, 0))
        for btn in self.buttonList:
            #buttons
            if btn.getIsPressed():
                screen.blit(btn.getImgPressed(), (btn.getX(), btn.getY()))
            else:
                screen.blit(btn.getImgUnpressed(), (btn.getX(), btn.getY()))
        
        #second for-loop to print item on mouse in front of buttons
        for btn in self.buttonList:
            #MouseImage
            if btn.getIsImgOnMouse():
                screen.blit(btn.getMouseImage().getRotObject(),(mouseX - btn.getMouseImage().getRotObject().get_width()/2, mouseY - btn.getMouseImage().getRotObject().get_height()/2))
            if btn.getMouseImage().getIsRotating():
                btn.getMouseImage().rotate()
                
                
                
                
