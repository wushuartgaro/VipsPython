# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 21:07:48 2018

@author: Hard-
"""

from SeparatorVo import SeparatorVo

class WeightRule:
    distance = 50
    
    @staticmethod
    def initialize(passed_nodeList):
        global nodeList 
        nodeList = passed_nodeList
    
    """
    The greater the distance between blocks on different side of the separator, 
	 the higher the weight.
    """
    @staticmethod
    def rule1(sep):
        if sep.Type == SeparatorVo.TYPE_HORIZ:
            #questions
            sep.weight = (sep.weight + sep.height/WeightRule.distance) 
        elif sep.Type == SeparatorVo.TYPE_VERTICAL:
            sep.weight = (sep.weight + sep.weight/WeightRule.distance)
    
    """
    If a visual separator is overlapped with some certain HTML tags (e.g., the <HR> HTML tag), 
	 its weight is set to be higher.
    """
    @staticmethod
    def rule2(sep, hrList):
        for block in hrList:
            box = block.boxs[0]
            RBX = sep.x + sep.width
            RBY = sep.y + sep.height
            HRRBX = box.visual_cues['bounds']['x'] + box.visual_cues['bounds']['width']
            HRRBY = box.visual_cues['bounds']['y'] + box.visual_cues['bounds']['height']
            if sep.x <= box.visual_cues['bounds']['x'] and box.visual_cues['bounds']['y']  and RBX>HRRBX and RBY>HRRBY:
                sep.weight += 1
            
    """
    If background colors of the blocks on two sides of the separator are different ,
	 the weight will be increased.
    
    """
    @staticmethod
    def rule3(sep):
        oneBox = sep.oneSide.boxs[0]
        otherBox = sep.otherSide.boxs[0]
        
        if oneBox.nodeType == 1 and otherBox.nodeType == 1:
            oneColor = oneBox.visual_cues['background-color']
            otherColor = otherBox.visual_cues['background-color']
            if oneColor != otherColor:
                sep.weight += 1
            
            
    """
    For horizontal separators, 
    if the differences of font properties such as font size and font weight 
    are bigger on two sides of the separator,the weight will be increased. 
    Moreover,the weight will be increased if the font size of the block above the 
    separator is smaller than the font size of the block below the separator.
    """
    @staticmethod
    def rule4(sep):
        if sep.Type == SeparatorVo.TYPE_HORIZ:
            oneBox = sep.oneSide.boxs[0]
            otherBox = sep.otherSide.boxs[0]
            
            oneSize = oneBox.visual_cues['font-size']
            otherSize = otherBox.visual_cues['font-size']
            if oneSize < otherSize:
                    sep.weight +=1
            #question
            if oneBox.nodeType == 1 and otherBox.nodeType == 1:
                oneWeight = oneBox.visual_cues['font-weight']
                otherWeight = otherBox.visual_cues['font-weight']
                if oneSize != otherSize and oneWeight != otherWeight:
                    sep.weight +=1

    
    """
    For horizontal separators, 
	 when the structures of the blocks on the two sides of the separator are very similar 
	 (e.g. both are text), the weight of the separator will be decreased.
    """
    @staticmethod
    def rule5(sep):
        if sep.Type == SeparatorVo.TYPE_HORIZ:
            oneBox = sep.oneSide.boxs[0]
            otherBox = sep.otherSide.boxs[0]
            oneName = oneBox.nodeName
            otherName = otherBox.nodeName
            if oneName == otherName:
                sep.weight -= 1