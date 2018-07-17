# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 17:19:23 2018

@author: Hard-
"""

class SeparatorVo:
    TYPE_HORIZ = 1
    TYPE_VERTICAL = 2
    
    x = 0
    y = 0
    width = 0
    height = 0
    weight = 7
    Type = 0
    oneSide = None
    otherSide = None
    
    def __init__(self, x , y, width, height, Type):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.Type = Type
        
    def compareTo(self, o):
        return self.weight - o.weight
    
    def equals(self, obj):
         if isinstance(obj,SeparatorVo):
             if obj.Type == SeparatorVo.TYPE_VERTICAL:
                 if obj.x == self.x and obj.width == self.width:
                     return True
        
         return self == obj
    
    