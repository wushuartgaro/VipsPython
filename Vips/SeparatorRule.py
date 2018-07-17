# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 18:37:29 2018

@author: Hard-
"""

class SeparatorRule:
    
    """
    a) If the horizontal block is contained in the separator, split the separator;
    """
    @staticmethod
    def horizontalRule1(block, sep):
        y = block.y
        if y > sep.y and (block.height + y) < (sep.height + sep.y):
            return True
        return False
    
    """
    c) If the horizontal block covers the separator, remove the separator.
    """
    @staticmethod
    def horizontalRule2(block, sep):
        y = block.y
        if y < sep.y and (block.height + y) > (sep.height + sep.y):
            return True
        return False
    
    
    """
    b) If the horizontal block crosses with the separator, update the separator's parameters;
    """
    @staticmethod
    def horizontalRule3(block, sep):
        y = block.y
        LBY = y + block.height
        sepRLY = sep.y + sep.height
        if y < sep.y and LBY > sep.y and LBY < sepRLY:
            return True
        return False
    
    """
    b) If the horizontal block crosses with the separator, update the separator's parameters;
    """
    @staticmethod
    def horizontalRule4(block, sep):
        y = block.y
        LBY = y + block.height
        sepLBY = sep.y + sep.height
        if y > sep.y and y < sepLBY and LBY > sepLBY:
            return True
        return False
    
    """
    a) If the vertical block is contained in the separator, split the separator;
    """
    @staticmethod
    def verticalRule1(block, sep):
        x = block.x
        if x > sep.x and (block.width + x) < (sep.width + sep.x):
            return True
        return False
    
    """
    c) If the block covers the separator, remove the separator.
    """
    @staticmethod
    def verticalRule2(block, sep):
        x = block.x
        if (x < sep.x and (block.width + x) > (sep.width + sep.x)) and (block.y < sep.y and (block.y + block.height) < (sep.y + sep.height)):
            return True
        return False
    
    """
    b) If the vetical block crosses with the separator, update the separator's parameters
    """   
    @staticmethod 
    def verticalRule3(block, sep):
        x = block.x
        rightX = x + block.width
        sepRightX = sep.x + sep.width
        if x < sep.x and rightX > sep.x and rightX < sepRightX: 
            return True
        return False
    
    
    """
    b) If the vetical block crosses with the separator, update the separator's parameters
    """  
    @staticmethod  
    def verticalRule4(block, sep):
        x = block.x
        rightX = x + block.width
        sepRightX = sep.x + sep.width
        if x > sep.x and x < sepRightX and rightX > sepRightX: 
            return True
        return False