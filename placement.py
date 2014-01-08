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
from util import Log
from config import *

class Placement:
    def __init__(self, colormap, pos):
        self.colormap = colormap.copy()
        self.placedMap = pygame.Surface(RIVERBED_SIZE)
        self.placedMap.fill((255,0,255))
        self.itemsPlaced = []
        self.itemsPos = []
        self.pos = pos
        
    def _blitAllItems(self):
        for i in range(0,len(self.itemsPlaced)):
            self.placedMap.blit(self.itemsPlaced[i], self.itemsPos[i])
            
    def undo(self):
        if len(self.itemsPlaced) != 0:
            self.itemsPlaced = self.itemsPlaced[:-1]
            self.itemsPos = self.itemsPos[:-1]
    
    def deleteItems(self):
        self.itemsPlaced = []
        self.itemsPos = []   
    

    def show(self, dest, img):
        dest.blit(self.colormap, self.pos)
        dest.blit(self.placedMap, self.pos)
        dest.blit(img, (pygame.mouse.get_pos()[0]-img.get_size()[0]/2, pygame.mouse.get_pos()[1]-img.get_size()[1]/2))
    
    
    def itemFitOnScreen(self, img):
        self._blitAllItems()
        #left hand corner of img
        img_pos_in_win = ( pygame.mouse.get_pos()[0]-img.get_size()[0]/2, pygame.mouse.get_pos()[1]-img.get_size()[1]/2)
        place_zone = pygame.Rect(self.pos[0],self.pos[1],RIVERBED_SIZE[0],RIVERBED_SIZE[1])
        Log("Click @ "+str(img_pos_in_win))

        if place_zone.collidepoint(img_pos_in_win):
            img_pos_in_win = (img_pos_in_win[0]-self.pos[0],img_pos_in_win[1]-self.pos[1])

            for y in range(0, img.get_height()):
                for x in range(0, img.get_width()):
                    if img.get_at((x,y))[3] != 0:
                        try:
                            if self.colormap.get_at(( img_pos_in_win[0]+x, img_pos_in_win[1]+y )) != (0,255,0):
                                Log("Picture not entirely on colormap"+str(img.get_at((x,y))))
                                return False
                            if self.placedMap.get_at(( img_pos_in_win[0]+x, img_pos_in_win[1]+y )) != (255,0,255):
                                Log("Cannot be placed there (already placed sth)")
                                return False
                        except:
                            Log("Picture outside place zone.")
                            return False
        else:
            Log("Outside place zone.")
            self.placedMap.fill((255,0,255))
            return False
     
        self.itemsPos.append(img_pos_in_win)
        img_pos_in_win = (img_pos_in_win[0]+self.pos[0],img_pos_in_win[1]+self.pos[1])
        self.placedMap.fill((255,0,255))
        self.itemsPlaced.append(img.copy())  
        Log("Inside place zone.")
        return True