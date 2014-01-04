# -*- coding: UTF-8 -*-

import pygame
from util import show_popup
from config import *

LEFT = 1
RIGHT = 3

class Button:
    def __init__(self, posXY, is_pressed, img_unpressed, img_pressed, mouse_image = None, is_img_on_mouse = None):
            self.posXY = posXY
            self.width = img_pressed.get_width()
            self.height = img_pressed.get_height()
            self.is_pressed = is_pressed
            self.img_pressed = img_pressed
            self.img_unpressed = img_unpressed
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
            self.buttonList.append(Button(item[0], False, item[1], item[2]))
    
    def blitter(self, screen, mouseX, mouseY):
        for btn in self.buttonList:
            #buttons
            if btn.getIsPressed():
                screen.blit(btn.getImgPressed(), (btn.getX(), btn.getY()))
            else:
                screen.blit(btn.getImgUnpressed(), (btn.getX(), btn.getY()))

    def eventHandler(self, event, mouseX, mouseY, WoodnStoneBtnList, RiverbedSize, screen):
        if event.type == pygame.MOUSEBUTTONDOWN and self.buttonList[0].mouseOnButton(mouseX, mouseY) and event.button == LEFT:
            self.buttonList[0].setIsPressed(True)
            if WoodnStoneBtnList.getBufferArrayCount() > 0:
                del WoodnStoneBtnList.getBufferArray()[len(WoodnStoneBtnList.getBufferArray())-1]
                WoodnStoneBtnList.setBufferArrayCount(WoodnStoneBtnList.getBufferArrayCount()-1)
                WoodnStoneBtnList.setBuffer()
        
        #SAVE-BUTTON:
        #TODO check wether files exist 
        if event.type == pygame.MOUSEBUTTONDOWN and self.buttonList[1].mouseOnButton(mouseX, mouseY) and event.button == LEFT:
            self.buttonList[1].setIsPressed(True) 
            imageToSave = pygame.Surface(RiverbedSize, pygame.SRCALPHA, 32)
            #CLEAR(imageToSave)
            imageToSave.blit(SCREEN, dest=(0,0), area=(20,85,690,490))
            pygame.image.save(imageToSave, "testImage.png")
            
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
        self.bufferArrayCount = 0
        for item in infoList:
            self.buttonList.append(Button(item[0], False, item[1],  item[2], item[3], False))
    
    def getButton(self, index):
        return self.buttonList[index]
            
    def getBufferArrayCount(self):
        return self.bufferArrayCount
    
    def setBufferArrayCount(self, _count):
        self.bufferArrayCount = _count
    
    def getBufferArray(self):
        return self.bufferArray
    
    def isButtonClicked(self):
        for btn in self.buttonList:
            if btn.getIsImgOnMouse():
                return True
        return False
    
    def setBuffer(self):
        if self.bufferArrayCount == 0:
            self.buffer.fill((0,0,0,0))
        else:
            self.buffer = self.bufferArray[self.bufferArrayCount]

    
    #handles the events
        #- Blit Image to buffer
        #- Image to Mouse
        #- rotation
    def eventHandler(self, event, mouseX, mouseY, img_pos):
        for btn in self.buttonList:
            #Blit Image to Buffer
            if event.type == pygame.MOUSEBUTTONDOWN and btn.getIsImgOnMouse() and event.button == LEFT:
                if img_pos:
                    self.buffer.blit(btn.getMouseImage().getRotObject(), img_pos)
                    self.bufferArray.append(self.buffer.copy())
                    self.bufferArrayCount += 1
                    btn.setIsImgOnMouse(False)
            
            #Image to Mouse
            if event.type == pygame.MOUSEBUTTONDOWN and btn.mouseOnButton(mouseX, mouseY) and btn.getIsImgOnMouse() == False and event.button == LEFT:
                btn.setIsPressed(True)

            if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                btn.setIsPressed(False)
                if btn.mouseOnButton(mouseX, mouseY) and btn.getIsImgOnMouse() == False:
                    #TODO: show popup, return and blit input
                    show_popup()
                    btn.getMouseImage().setRotAngle(0)
                    btn.getMouseImage().setRotObject(btn.getMouseImage().getOriginalObject())
                    btn.setIsImgOnMouse(True)
                    print "clicked"
                
  
            
            #rotation  
            if event.type == pygame.MOUSEBUTTONDOWN and btn.getIsImgOnMouse() and event.button == RIGHT:
                btn.getMouseImage().setIsRotating(True)
            if event.type == pygame.MOUSEBUTTONUP and btn.getIsImgOnMouse() and event.button == RIGHT:
                btn.getMouseImage().setIsRotating(False)

    #blits the buffer, buttons and MouseImage on the screen            
    def blitter(self, screen, mouseX, mouseY):
        #buffer
        screen.blit(self.bufferArray[self.bufferArrayCount], (0, 0))
        for btn in self.buttonList:
            #buttons
            if btn.getIsPressed():
                screen.blit(btn.getImgPressed(), (btn.getX(), btn.getY()))
            else:
                screen.blit(btn.getImgUnpressed(), (btn.getX(), btn.getY()))
            #MouseImage
            if btn.getIsImgOnMouse():
                screen.blit(btn.getMouseImage().getRotObject(),(mouseX - btn.getMouseImage().getRotObject().get_width()/2, mouseY - btn.getMouseImage().getRotObject().get_height()/2))
            if btn.getMouseImage().getIsRotating():
                btn.getMouseImage().rotate()
                
                
                
                
