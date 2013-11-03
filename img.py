# -*- coding: UTF-8 -*-
import pygame


class Img:
    
    def __init__(self, posX, posY, visible, is_rotating, rot_angle, rot_object, original_object):
        self.posX = posX
        self.posY = posY
        self.visible = visible
        self.is_rotating = is_rotating
        self.rot_angle = rot_angle
        self.rot_object = rot_object
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
        
    def getOriginalObject(self):
        return self.original_object
    
    def setOriginalObject(self, _original_object):
        self.original_object = _original_object
        
    def rotate(self):
        self.setRotAngle(self.getRotAngle()+1)
        self.setRotObject(pygame.transform.rotate(self.original_object, self.getRotAngle()))
        
    def place(self, mouseX, mouseY):
        self.setX(mouseX - self.getRotObject().get_width()/2)
        self.setY(mouseY - self.getRotObject().get_height()/2)
        self.setVisible(True)
        self.setIsRotating(False)
    