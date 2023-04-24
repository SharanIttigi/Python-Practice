# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 12:37:05 2023

@author: WIN10 PRO 22H2
"""
import random


class Blob:
    def __init__(self,color,x_boundary,y_boundary):
        self.color=color
        self.x=random.randrange(0,x_boundary)
        self.y=random.randrange(0,y_boundary)
        self.size=random.randrange(4,8)
        self.x_boundary=x_boundary
        self.y_boundary=y_boundary
       
        
    def move(self):
        self.move_x=random.randrange(-1,2)
        self.move_y=random.randrange(-1,2)
        self.x+=self.move_x
        self.y+=self.move_y
        
        
        
        
    def move_boundary(self):
        if self.x<=0:
            self.x=0
        elif self.x>self.x_boundary:
            self.x=self.x_boundary
         
        if self.y<=0:
            self.y=0
        elif self.y>self.y_boundary:
            self.y=self.y_boundary
        
        
