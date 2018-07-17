# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 21:06:18 2018

@author: Hard-
"""
from WeightRule import WeightRule

class SeparatorWeight:
    
    def __init__(self, nodeList):
        WeightRule.initialize(nodeList)
    
    def service(self, separatorList, hrList):
        for sep in separatorList:
            if sep.oneSide == None or sep.otherSide == None:
                continue           
            
            WeightRule.rule1(sep)
            WeightRule.rule2(sep,hrList)
            WeightRule.rule3(sep)
            WeightRule.rule4(sep)
            WeightRule.rule5(sep)
    
    