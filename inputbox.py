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

##### CLASS INPUTBOX #####
# Constructor:
#     InputBox(pos, buffer, color = BOX_EMPTY_COLOR, padding = BOX_PADDING, max_char = None) <=>
#       pos : position of the inputbox
#       buffer : pygame.Surface (transparent) to blit the box on (to update the box properly)
#       color : Border color
#       padding : size of padding in the box
#       max_char : maximum character number in one line. If None it's 1000
#       max_size : input box ist static to this pixel size
#
# Methods:
#    blit( dest, pos = None ) <=> blits the content of the inputbox to dest
#                                 if pos != None it's blit to the inputbox position. pos is a 2-tuple (x,y)
#    isFocus() <=> True if inputbox is selected. False if not.
#    makeFocus() <=> put's the box into focus to write in it.
#    releaseFocus() <=> releases the focus of the current box
#    putChar(char) <=> adds char to string
#    makeRow() <=> creates second row
#    hasSecondRow() <=> True if there is a second row in use. False if not
#    isEmpty() <=> True if the box has no content
#    delChar() <=> deletes the last character added to the inputbox
#    getString()  <=> return the content string
#    isMouseInside <=> True if mouse is over inputbox rect
#####

##### CLASS EventInputBoxes #####
# Constructor:
#    EventInputBoxes(pos_lst, screen) <=>
#       pos_lst : list of positions (2-tuple) 
#       screen : screen to blit on.
#
# Methods:
#    updateBoxes() <=> refreshes the inputboxes and blits them first to buffer and then to the screen
#    handelEvent(event) <=> event is an element from pygame.event.get(). 'handleEvent' checks for events
#                                    important for the inputboxes e.g. Key presses and mouse clicks
#
#    nextBox() <=> jump to the next box in the list. This box will be focused.
#####

####TODO: 
#### - Inputboxes show tabsymbol


import pygame, pygame.font, re
import string
from config import *

class InputBox:
    def __init__(self, pos, buffer, color = BOX_COLORS, font_color = FONT_COLOR, padding = BOX_PADDING, max_char = None, max_size = None, enable_rows = True):
        self.buffer = buffer
        self.pos = pos
        self.rect = self.pos + ( max_size if max_size else FONT_SIZE + 4*padding, FONT_SIZE + 2*padding )
        self.colors = color
        self.colorid = 2 # 0:no focus,1:focus,2:empty
        self.fontcolor = font_color
        self.focus = False
        self.string = []
        self.string2 = []
        self.string_rend = None
        self.string2_rend = None
        self.stringX = 0
        self.stringY = 0
        self.string2Y = 0
        self.padding = padding
        self.SecondRow = False
        self.secondRowPadding = 4
        self.max_char = 1000 if max_char == None else max_char
        self.max_size = max_size
        self.enable_rows = enable_rows
        
        
    #blits the inputbox to the buffer and then to the screen
    def _blitToBuffer(self, dest):    
        if not self.isEmpty():
            self._renderString()
            if self.colors[self.colorid]:
                pygame.draw.rect(self.buffer, self.colors[self.colorid], self.rect, 2)
            self.buffer.blit( self.string_rend , (self.stringX, self.stringY) )
            if self.SecondRow:
                self.buffer.blit( self.string2_rend , (self.stringX, self.string2Y) )
            dest.blit(self.buffer, (0,0))
        else:
            self.blitEmpty(dest)
        
    def blit(self, dest, pos = None):
        if not self.isEmpty():
            self._renderString()
            if not pos:
                dest.blit( self.string_rend , (self.stringX, self.stringY) )
                if self.SecondRow:
                    dest.blit( self.string2_rend , (self.stringX, self.string2Y) )
            else:
                dest.blit( self.string_rend , pos )
                if self.SecondRow:
                    dest.blit( self.string2_rend , (pos[0], pos[1] + self.string_rend.get_height() + self.secondRowPadding) )
        else:
            self.blitEmpty(dest)
            
    
    def _renderString(self):  
        if not self.isEmpty():
            #render string an d calculate position for the first string
            self.string_rend = pygame.font.Font( FONT, FONT_SIZE).render( string.join(self.string,""), True, self.fontcolor )
            self.stringX = self.rect[0] + self.padding
            self.stringY = self.rect[1] + self.padding
            self.rect = ( self.rect[0], self.rect[1],\
                            self.string_rend.get_width() + 2*self.padding,\
                            self.string_rend.get_height() + 2*self.padding ) 
                            
            #render string an d calculate position for the first string
            if self.SecondRow:
                self.string2_rend = pygame.font.Font( FONT, FONT_SIZE).render( string.join(self.string2,""), True, self.fontcolor )
                self.string2Y = self.stringY + self.string_rend.get_height() + self.secondRowPadding
                lengthX = self.string_rend.get_width() if self.string_rend.get_width() > self.string2_rend.get_width() else self.string2_rend.get_width()
                self.rect = ( self.rect[0], self.rect[1],\
                             lengthX + 2*self.padding,\
                            self.string_rend.get_height() + self.string2_rend.get_height() + self.secondRowPadding + 2*self.padding )
            
            if self.max_size:
                self.rect = (self.rect[0],\
                            self.rect[1],\
                            self.max_size,\
                            self.rect[3])
            
    def blitEmpty(self, dest):
        rect = self.pos + ( self.max_size if self.max_size else FONT_SIZE + 4*self.padding, FONT_SIZE + 2*self.padding )
        pygame.draw.rect(dest, self.colors[self.colorid], rect, 2)

   
    def isFocus(self):
        return self.focus
    
    def makeFocus(self):
        self.focus = True
        self.colorid = 1 #BOX_FOCUSED_COLOR
        
    def releaseFocus(self):
        self.focus = False
        if self.isEmpty():
            self.colorid = 2 #BOX_EMPTY_COLOR
        else:
            self.colorid = 0 #BOX_COLOR
   
    def putChar(self, char): 
        if char == u'\u1e9e': #capital sharp s
            char = u'\?'
        if self.SecondRow and len(self.string2) < self.max_char:
            self.string2.append(char)
        elif len(self.string) < self.max_char:
            self.string.append(char)
        self._renderString()
        
        if self.max_size:
            if self.string_rend.get_width() + 2*self.padding > self.max_size or\
                self.SecondRow and self.string2_rend.get_width() + 2*self.padding > self.max_size:
                self.delChar()
                self._renderString()
        
    def makeRow(self):
        if self.enable_rows:
            self.SecondRow = True
        
    def hasSecondRow(self):
        return self.SecondRow

    def isEmpty(self):
        return len(self.string) == 0 and len(self.string2) == 0
    
    def delChar(self):
        if self.isEmpty() and not self.isFocus():
            self.colorid = 2 #BOX_EMPTY_COLOR
        if len(self.string2) != 0:
            self.string2 = self.string2[0:-1]
        else:
            self.string = self.string[0:-1]
            self.SecondRow = False
        self._renderString()
            
    def getString(self):
        return string.join(self.string,"")+"\n"+string.join(self.string2,"") if self.hasSecondRow() \
                else string.join(self.string,"")
            
    def isMouseInside(self):
        mouse = pygame.mouse.get_pos()
        return  mouse[0] > self.rect[0] and mouse[0] < self.rect[0]+self.rect[2] \
                    and mouse[1] > self.rect[1] and mouse[1] < self.rect[1]+self.rect[3]
                    
    def handleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.isMouseInside():
                self.makeFocus()
            else:
                if self.isFocus():
                    self.releaseFocus()
        if event.type == pygame.KEYDOWN:
            if self.isFocus():
                if event.key == pygame.K_ESCAPE:
                    self.releaseFocus()
                elif event.key == pygame.K_RETURN:
                    #if box.hasSecondRow():
                    #    box.releaseFocus()
                    if not self.hasSecondRow():
                        self.makeRow()
                elif event.key == pygame.K_BACKSPACE:
                    self.delChar()
                elif event.key not in FORBIDDEN_KEYS:
                    self.putChar(event.unicode)    
    def update(self, dest):
        self._blitToBuffer(dest)
    def reset(self):
        self.string = []
        self.string2 = []
        self.SecondRow = False
        self.colorid = 2
        
                    
                    
                    
class EventInputBoxes:
    def __init__(self, pos_lst, screen, buffer = BUFFER):
        self.buffer = buffer
        self.boxes = []
        for pos in pos_lst:
            if len(pos) == 2:
                self.boxes.append( InputBox(pos, self.buffer) )
            if len(pos) == 3:
                self.boxes.append( InputBox(pos, self.buffer, max_size = pos[2]) )
        self.amount = len(self.boxes)
        self.screen = screen
        
        
    def updateBoxes(self):
        for box in self.boxes:
            box.update(self.screen)
    
    def handleEvent(self, event):
        for box in self.boxes:
            box.handleEvent(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB: #always?
                self.nextBox()
                        
    def nextBox(self):
        current = 0
        for box in self.boxes:
            if box.isFocus():
                box.releaseFocus()
                break
            current += 1
        self.boxes[(current+1)%self.amount].makeFocus()
    
    def reset(self):
        for box in self.boxes:
            box.reset()
    
                        