# -*- coding: utf-8 -*-
"""
Created on Tue May 29 12:37:05 2018

@author: Hard-
"""
import sys
import BlockVo
import BlockRule

class BlockExtraction:
    
    html = None
    blockList = []
    hrList = []
    cssBoxList = dict()
    block = None
    count = 0
    count1 = 0
    count2 = 0
    count3 = 1
    all_text_nodes = []

    def __init__(self):
        self.block = BlockVo.BlockVo()
                
    def service(self, url, nodeList):
        BlockRule.BlockRule.initialize(nodeList)
        body = nodeList[0]
        self.initBlock(body, self.block)  
        print("-----Done Initialization-----")
        self.count3 = 0
        self.dividBlock(self.block)
        print(self.count2)       
        print("-----Done Division-----")
        BlockVo.BlockVo.refreshBlock(self.block)
        print("-----Done Refreshing-----")
        self.filList(self.block)
        print("-----Done Filling-----")
        #self.checkText()
        return self.block
        
    def initBlock(self, box, block):
        block.boxs.append(box)
        print(self.count,"####Here Name=",box.nodeName)
        self.count+=1
            
        if(box.nodeName == "hr"):
            self.hrList.append(block)
            self.count1 = 0
        if box.nodeType != 3:
            subBoxList = box.childNodes
            for b in subBoxList:
                try:
                    if b.nodeName != "script" and b.nodeName != "noscript" and b.nodeName != "style":
                        #print(self.count1," : ",b.nodeName,", ",box.nodeName)
                        self.count1+=1
                        bVo = BlockVo.BlockVo()
                        bVo.parent = block
                        block.children.append(bVo)
                        self.initBlock(b, bVo)       
                except AttributeError:
                    print(b,",",b.nodeType)
                    sys.exit(0)
            
    def dividBlock(self, block):
        self.count2+=1
        print (self.count2)
        if(block.isDividable and BlockRule.BlockRule.dividable(block)):
            block.isVisualBlock = False         
            for b in block.children:
                self.count3+=1
                print(self.count3)
                self.dividBlock(b)
                        
    def filList(self, block):
        if block.isVisualBlock:
            self.blockList.append(block)
        else:
            for blockVo in block.children:
                self.filList(blockVo)

    def checkText(self):
        for blockVo in self.blockList:
            removed = True
            for box in blockVo.boxs:
                if box.nodeType == 3:
                    if box.parentNode.nodeName != "script" and box.parentNode.nodeName != "noscript" and box.parentNode.nodeName != "style":
                         if not box.nodeValue.isspace() or box.nodeValue == None:
                             removed = False
            if(removed):
                self.blockList.remove(blockVo)

        