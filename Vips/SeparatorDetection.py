# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 17:16:53 2018

@author: Hard-
"""
import sys

from SeparatorVo import SeparatorVo
from SeparatorRule import SeparatorRule

class SeparatorDetection:
    width = 0
    height = 0
    separatorType = 0
    separatorList = None
    count = 0
    
    def __init__(self, width, height):
        self.separatorList = []
        self.width = width
        self.height = height
    
    def service(self, blocks, separatorType):
        self.separatorType = separatorType
        self.separatorList.clear()
        self.oneStep()
        self.twoStep(blocks)
        self.threeStep()
        print (str(self.separatorType) + "-SeparatorVo.list.size::"+ str(len(self.separatorList)))
        return self.separatorList
        
    """
    Initialize the separator list. The list starts with only one separator (P be , P ee ) whose
    start pixel and end pixel are corresponding to the borders of the pool.
    """
    def oneStep(self):
        separator = SeparatorVo(0,0,self.width,self.height,self.separatorType)
        self.separatorList.append(separator)
    
    """
    For every block in the pool, the relation of the block with each separator is evaluated
	 a) If the block is contained in the separator, split the separator;
	 b) If the block crosses with the separator, update the separator's parameters;
	 c) If the block covers the separator, remove the separator.
    """
    
    def twoStep(self, blocks):
        if(len(self.separatorList)>0):
            if (self.separatorType == SeparatorVo.TYPE_HORIZ):
                self.horizontalDetection(blocks)
            else:
                self.verticalDetection(blocks)
    
    """
    Remove the four separators that stand at the border of the pool
    """
    
    def threeStep(self):
        temp = []
        temp.extend(self.separatorList)
        if self.separatorType == SeparatorVo.TYPE_HORIZ:
            for sep in temp:
                if sep.x == 0 and (sep.y == 0 or (sep.y + sep.height) == self.height):
                    self.separatorList.remove(sep)
        else:
            for sep in temp:
                if sep.y == 0 and (sep.x == 0 or (sep.x + sep.width) == self.width):
                    self.separatorList.remove(sep)
    
    def horizontalDetection(self, blocks):
        for block in blocks:
            temp = []
            temp.extend(self.separatorList)
            for sep in temp:
                self.count+=1
                print(")",self.count)
                if SeparatorRule.horizontalRule1(block, sep):
                    y = block.y + block.height
                    newSep = SeparatorVo(0, y, self.width, (sep.y + sep.height) - y, self.separatorType)
                    if newSep.height != 0:
                        newSep.oneSide = block
                        self.separatorList.append(newSep)
                    
                    separator = sep
                    #self.separatorList[self.separatorList.index(sep)]
                    separator.height = block.y - separator.y
                    if separator.height == 0:
                        self.separatorList.remove(separator)
                    else:
                        separator.otherSide = block
                elif SeparatorRule.horizontalRule2(block, sep):
                    self.separatorList.remove(sep)
                elif SeparatorRule.horizontalRule3(block, sep):
                    separator = sep
                    #self.separatorList[self.separatorList.index(sep)]
                    originalY = separator.y
                    separator.y = block.y + block.height
                    separator.height = separator.height + originalY - separator.y
                    separator.oneSide = block
                elif SeparatorRule.horizontalRule4(block, sep):
                    separator = sep
                    #self.separatorList[self.separatorList.index(sep)]
                    separator.height = block.y - separator.y
                    separator.otherSide = block
                else:
                    continue
        
    def verticalDetection(self, blocks):
        self.separatorList.clear()
        for b1 in blocks:
            leftMinW = sys.maxsize
            leftX = 0
            leftY = 0
            leftW = 0
            leftH = 0
            
            rightMinW = sys.maxsize
            rightX = 0
            rightY = 0
            rightW = 0
            rightH = 0
            
            for b2 in blocks:
                if b1 == b2:
                    continue
                RBX1 = b1.x + b1.width
                RBX2 = b2.x + b2.width
                RBY1 = b1.y + b1.height
                RBY2 = b2.y + b2.height
                
                if RBX2<b1.x:
                    X = b2.x + b2.width
                    W = b1.x - X
                    
                    sep = SeparatorVo(0,0,b1.x,b1.height,SeparatorVo.TYPE_HORIZ)
                    if SeparatorRule.verticalRule1(b2,sep):
                        if W < leftMinW:
                            leftMinW = W
                            leftX = X
                            leftY = b1.y
                            leftW = W
                            leftH = b1.height
                    elif SeparatorRule.verticalRule2(b2,sep):
                        if W < leftMinW:
                            leftMinW = W
                            leftX = X
                            leftY = b2.y
                            leftW = W
                            leftH = b2.height
                    elif SeparatorRule.verticalRule3(b2,sep):
                        if W < leftMinW:
                            leftMinW = W
                            leftX = X
                            leftY = b2.y
                            leftW = W
                            leftH = RBY1-b2.y
                    elif SeparatorRule.verticalRule4(b2,sep):
                        if W < leftMinW:
                            leftMinW = W
                            leftX = X
                            leftY = b1.y
                            leftW = W
                            leftH = RBY2-b1.y
                elif b2.x > RBX1:
                    X = b1.x + b1.width
                    W = b2.x - X
                    sep = SeparatorVo(b1.x+b1.width, b1.y, self.width, self.height, SeparatorVo.TYPE_HORIZ)
                    if SeparatorRule.verticalRule1(b2,sep):
                        if W < rightMinW:
                            rightMinW = W
                            rightX = X
                            rightY = b1.y
                            rightW = W
                            rightH = b1.height
                    elif SeparatorRule.verticalRule2(b2,sep):
                        if W < rightMinW:
                            rightMinW = W
                            rightX = X
                            rightY = b2.y
                            rightW = W
                            rightH = b2.height
                    elif SeparatorRule.verticalRule3(b2,sep):
                        if W < rightMinW:
                            rightMinW = W
                            rightX = X
                            rightY = b2.y
                            rightW = W
                            rightH = RBY1-b2.y
                    elif SeparatorRule.verticalRule4(b2,sep):
                        if W < rightMinW:
                            rightMinW = W
                            rightX = X
                            rightY = b1.y
                            rightW = W
                            rightH = RBY2-b1.y
                
            if leftMinW < sys.maxsize:
                separator = SeparatorVo(leftX,leftY,leftW,leftH,SeparatorVo.TYPE_VERTICAL)
                self.separatorList.append(separator)
            if rightMinW < sys.maxsize:
                separator = SeparatorVo(rightX,rightY,rightW,rightH,SeparatorVo.TYPE_VERTICAL)
                self.separatorList.append(separator)
                
        self.mergeSeparator()
        
    def mergeSeparator(self):
        removed_list = []
        removed_index = []
        temp1 = []
        temp1.extend(self.separatorList)
        for i in range (0, len(temp1)):
            sep1 = temp1[i]
            for j in range(i+1, len(temp1)):
                sep2 = temp1[j]
                if sep1.equals(sep2) and (abs(sep1.y-sep2.y) < 100):
                    removed_index.append(j)
                    if sep2.y > sep1.y:
                        #question
                        sep1.y = sep1.y
                        sep1.height = abs(sep1.y - sep2.y) + sep2.height
                    elif sep2.y < sep1.y:
                        sep1.y = sep2.y
                        sep1.height = abs(sep1.y - sep2.y) + sep1.height  
        for index in removed_index:
            removed_list.append(self.separatorList[index])
        
        for sep in removed_list:
            removed_list.remove(sep)