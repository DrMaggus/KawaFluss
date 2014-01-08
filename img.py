# -*- coding: utf-8 -*-
"""
* Copyright (C) 2013 Matthias Eiserloh & Markus Wolf
*
* This file is part of KawaFluss.
*
* KawaFluss is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation, version 3 of the License.
*
* KawaFluss is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along with KawaFluss. If not, see <http://www.gnu.org/licenses/>.
"""

import pygame


class Img:
    
    def __init__(self, posX, posY, visible, is_rotating, rot_angle, rot_object, font_object, original_object):
        self.posX = posX
        self.posY = posY
        self.visible = visible
        self.is_rotating = is_rotating
        self.rot_angle = rot_angle
        self.rot_object = rot_object
        self.font_object = font_object
        self.original_object = original_object
        
    def getX(self):
        return self.posX
    
    def setX(self, _posX):
        self.posX = _posX
        
    def getY(self):
        return self.posY
    
    def setY(self, _posY):
        self.posY = _posY

    def getVisible(self):
        return self.visible
    
    def setVisible(self, _visible):
        self.visible = _visible
        
    def getIsRotating(self):
        return self.is_rotating
    
    def setIsRotating(self, _is_rotating):
        self.is_rotating = _is_rotating
        
    def getRotAngle(self):
        return self.rot_angle
    
    def setRotAngle(self, _rot_angle):
        self.rot_angle = _rot_angle
        
    def getRotObject(self):
        return self.rot_object
    
    def setRotObject(self, _rot_object):
        self.rot_object = _rot_object
        
    def getFontObject(self):
        return self.font_object
    
    def setFontObject(self, _font_object):
        self.font_object = _font_object    
        
    def getOriginalObject(self):
        return self.original_object
    
    def setOriginalObject(self, _original_object):
        self.original_object = _original_object
        
    def rotate(self):
        self.setRotAngle(self.getRotAngle()+2)
        self.setRotObject(pygame.transform.rotate(self.font_object, self.getRotAngle()))
        
    def place(self, mouseX, mouseY):
        self.setX(mouseX - self.getRotObject().get_width()/2)
        self.setY(mouseY - self.getRotObject().get_height()/2)
        self.setVisible(True)
        self.setIsRotating(False)
    