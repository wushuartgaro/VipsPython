# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 21:42:04 2018

@author: Hard-
"""
from BlockVo import BlockVo

class ContentStructureConstruction:
    
    def service(self, sepList, block):
        if len(sepList) > 0:
            temp = []
            temp.extend(sepList)
            maxWeight = temp[len(temp)-1].weight
            print ("maxWeight::", maxWeight)
            for sep in temp:
                if maxWeight == sep.weight:
                    #print("####")
                    break
                if sep.oneSide != None and sep.otherSide != None:
                    one = sep.oneSide
                    other = sep.otherSide
                    newBlock = BlockVo()
                    newBlock.parent = one.parent
                    newBlock.boxs.extend(one.boxs)
                    newBlock.boxs.extend(other.boxs)
                    newBlock.children.extend(one.children)
                    newBlock.children.extend(other.children)
                    newBlock.Doc = sep.weight
                    newBlock.refresh()
                    one.parent.children.append(newBlock)
                    one.isVisualBlock = False
                    other.isVisualBlock = False
                    Sum = 0
                    for separator in temp:
                        if separator.oneSide == other:
                            separator.oneSide = newBlock
                            Sum+=1
                        if separator.otherSide == one:
                            separator.otherSide = newBlock
                            Sum+=1
                        if Sum == 2:
                            break
                    sepList.remove(sep)

